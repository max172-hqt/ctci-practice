# [2,4,6,10]
# 16

def count_sets(arr, total):
    return rec(arr, total, len(arr) - 1)


def rec(arr, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        return rec(arr, total, i-1)

    return rec(arr, total - arr[i], i-1) + rec(arr, total, i-1)


def count_sets_dp(arr, total):
    memo = {}
    res = dp(arr, total, len(arr) - 1, memo)
    print(memo)
    return res


def dp(arr, total, i, memo):
    key = f"{str(total)}:{i}"
    if key in memo:
        return memo[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        res = dp(arr, total, i-1, memo)
    else:
        res = dp(arr, total, i-1, memo) + dp(arr, total-arr[i], i-1, memo)
    memo[key] = res
    return res

if __name__ == "__main__":
    print(count_sets([2,4,6,10], 16))
    print(count_sets_dp([2,4,6,10], 16))


# Divide into two sub problems
# include the current number i or not
# sub problem 
# ; (arr, total - arr[i], i)
# total of subsets which add up to total and include the current number
# is equivalent to the total no of subsets which add up to total - current
# number and include the remaning numbers
# ; (arr, total, i)
