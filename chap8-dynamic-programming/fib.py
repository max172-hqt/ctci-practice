# def fib_recursive(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib_recursive(n - 1) + fib_recursive(n - 2)

# Top-down approach

# def fib(i):
#     def helper(i, memo):
#         if i == 0 or i == 1:
#             return i
#         if memo[i] == 0:
#             # Memoization here
#             memo[i] = helper(i-1, memo) + helper(i-2, memo)
#         return memo[i]
#     return helper(i, [0] * (i+1))

# Bottom-up approach
def fib(n):
    if n == 0 or n == 1:
        return n

    memo = [0]*(n+1) 
    memo[0] = 0    
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2]

if __name__ == "__main__":
    print(fib(5))
