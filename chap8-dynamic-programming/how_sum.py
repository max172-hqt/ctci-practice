def how_sum(candidates, target):
    if target < 0:
        return None
    if target == 0:
        return []
    for num in candidates:
        remainder = target - num
        curr = how_sum(candidates, remainder)
        if curr is not None:
            return curr + [num]
    return None

if __name__ == "__main__":
    print(how_sum([2,3], 1000))
