# best_sum(7, [5,4,3,7])

def best_sum(target, candidates):
    memo = {}
    def dp(target, memo):
        if target in memo:
            return memo[target]
        if target == 0:
            return []
        if target < 0:
            return None

        shortest = None
        for num in candidates:
            remainder = target - num
            curr = dp(remainder, memo)
            if curr is not None:
                res = curr + [num]  # Linear operation, worst case m (bunch of 1s)
                if shortest is None or len(res) < len(shortest):
                    shortest = res
        memo[target] = shortest
        return shortest
    return dp(target, memo)


# n: length of array
# m: target
# brute force
# time: O(n^m * m) ^m because of m levels in the tree
# space: O(m^2) each recursive call has its own shortest array

# memoized 
# time: Do not need to explore duplicate subtree because we use memo object
# max number of keys in memo object would be m
# need branch for every number in the array
# O(m^2 * n)
# space: O(m^2)

if __name__ == "__main__":
    print(best_sum(100, [1,2,5,25]))
