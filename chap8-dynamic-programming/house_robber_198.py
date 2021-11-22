# def rob(nums):
#     memo = {}
#     def dp(i, memo):
#         if i in memo:
#             return memo[i]
#         if i < 0:
#             return 0
#         res = max(nums[i] + dp(i-2, memo), dp(i-1, memo))
#         memo[i] = res
#         return res

#     return dp(len(nums)-1, memo)

# def rob(nums):
#     n = len(nums)
#     if n <= 2: return max(nums)
    
#     dp = [0] * n
#     dp[0] = nums[0]
#     dp[1] = nums[1]

#     for i in range(2, n):
#         dp[i] = max(dp[i-2], dp[i-3]) + nums[i] 
#     return max(dp[n-1],dp[n-2])

# def rob(nums):
#     n = len(nums)
#     if n <= 2: return max(nums)
    
#     dp = [0] * n
#     dp[0] = nums[0]
#     dp[1] = max(nums[0], nums[1])

#     for i in range(2, n):
#         dp[i] = max(nums[i] + dp[i-2], dp[i-1])
#     return dp[n-1]

def rob(nums):
    n = len(nums)
    if n <= 2: return max(nums)

    rob1 = nums[0]
    rob2 = max(nums[0], nums[1])

    for i in range(2, n):
        res = max(nums[i] + rob1, rob2)
        rob1 = rob2
        rob2 = res
    return rob2

if __name__ == '__main__':
    print(rob([2,1,1,2])) 