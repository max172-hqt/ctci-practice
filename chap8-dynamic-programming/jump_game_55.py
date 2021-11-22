def can_jump(nums):
    if len(nums) <= 1:
        return True
    dp = [0] * len(nums)
    dp[0] = nums[0]
    if dp[0] == 0:
        return False
    dp[1] = max(dp[0] - 1, nums[1])
    
    for i in range(2, len(nums)):
        if dp[i-1] < 1:
            return False
        dp[i] = max(nums[i], dp[i-1] - 1)
    return True


def can_jump(nums):
    farthest = 0  # farthest index we can reach
    
    for i in range(len(nums)):
        if farthest < i:
            return False
        farthest = max(farthest, nums[i] + i)
    return True