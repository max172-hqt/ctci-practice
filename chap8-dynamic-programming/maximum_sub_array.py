def max_sub_array(nums):
    curr_sum = 0
    max_sum = None 

    for num in nums:
        curr_sum += num
        if max_sum is None or curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


if __name__ == '__main__':
    print(max_sub_array([-3,5,5]))