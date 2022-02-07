def max_profit(nums):
    valley = nums[0]
    peak = -1
    total_profit = 0
    
    for i in range(1, len(nums)):
        if nums[i] < peak:
            total_profit += peak - valley
            valley = nums[i]
            peak = -1
            continue

        if nums[i] >= peak:
            peak = nums[i]
        if nums[i] < valley:
            valley = nums[i]

    if peak != -1:
        total_profit += peak - valley
        
    return total_profit


if __name__ == "__main__":
    print(max_profit([7,6,4,3,1]))