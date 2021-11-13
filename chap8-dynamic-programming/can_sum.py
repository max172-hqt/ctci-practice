def can_sum(target, candidates):
    memo = {}
    return dp(target, candidates, memo)

def dp(target, candidates, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in candidates:
        if dp(target-num, candidates, memo):
            memo[target] = True
            return True
        
    memo[target] = False
    return False

if __name__ == "__main__":
    print(can_sum(7, [2,3]))
    print(can_sum(7, [5,3,4,7]))
    print(can_sum(7, [2,4]))
    print(can_sum(8, [2,4,5]))
    print(can_sum(1000, [7,14,28]))
