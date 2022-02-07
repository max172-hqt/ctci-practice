def max_sub_array_circular(nums):
    # case 1 
    curr_sum, max_sum = float('-inf'), float('-inf')
    for num in nums:
        curr_sum += num
        curr_sum = max(curr_sum, num)
        max_sum = max(max_sum, curr_sum)

    # TODO: Case 2
    return max_sum

if __name__ == '__main__':
    print(max_sub_array_circular([5,-3,5]))