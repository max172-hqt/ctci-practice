class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, i):
        return self._coords[i]

    def __setitem__(self, i, val):
        self._coords[i] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other  # rely on __eq__ definition

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ == "__main__":
    a = Vector(5)
    a[1] = 10
    print(a + a)
    i = iter(a)
    print(next(i))
    print(next(i))
    print(next(i))
