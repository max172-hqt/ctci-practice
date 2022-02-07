def max_product(nums):
    min_neg = 1
    max_pos = 1
    best = max(nums)
    
    for num in nums:
        if num == 0:
            min_neg = 1
            max_pos = 1
            continue
        temp = max_pos
        # current max and current min of subarray from [start -> num] which includes num
        max_pos = max(num * max_pos, num * min_neg, num)
        # [-1 -8] we want the actual number -8, not -1
        min_neg = min(num * temp, num * min_neg, num)
        best = max(max_pos, best)
    return best


if __name__ == '__main__':
    print(max_product([2,0,-1]))