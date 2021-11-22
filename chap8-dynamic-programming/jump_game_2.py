# def jump(nums):
#     memo = {}
#     def dp(i, memo):
#         print(memo)
#         if i in memo:
#             return memo[i]
#         if i == 0 or i == 1:
#             return i
#         min_steps = None
#         for j in range(i-1,-1,-1):
#             if nums[j] + j >= i:
#                 num_steps = 1 + dp(j, memo)
#                 if min_steps is None or num_steps < min_steps:
#                     min_steps = num_steps
#         memo[i] = min_steps
#         return min_steps
#     return dp(len(nums) - 1, memo)

# def jump(nums):
#     if len(nums) <= 1:
#             return 0
        
#     dp = [1001] * len(nums)
#     dp[0] = 0
#     dp[1] = 1

#     for i in range(2, len(nums)):
#         for j in range(i-1,-1,-1):
#             if nums[j] + j >= i:
#                 dp[i] = min(dp[i], dp[j] + 1)
        
#     return dp[len(nums) - 1]

# Get the farthest point a block can get to
# Repeat for next block, defined by left and right
# Also, increase step by 1
def jump(nums):
    res = 0
    left = 0
    right = 0
    while right < len(nums) - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(nums[i] + i, farthest)
        left = right + 1
        right = farthest
        res += 1
    return res
        
        
if __name__ == '__main__':
    print(jump([2,3,1,1,4]))
