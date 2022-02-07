import math


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        step_sign = math.copysign(1, step)         
        self._len = max(0, 1 + (stop - start - step_sign) // step)
        self._start = start
        self._step = step
    
    def __len__(self):
        return self._len

    def __getitem__(self, j):
        if j < 0:
            j += len(self)
        
        if not 0 <= j < len(self):
            raise IndexError('index out of range')

        return self._start + self._step * j


if __name__ == '__main__':
    for i in Range(10, 1, -1):
        print(i)
    for i in range(10, 1, -1):
        print(i)
