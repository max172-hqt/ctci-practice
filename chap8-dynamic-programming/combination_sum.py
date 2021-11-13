def how_sum(candidates, target):
    candidates.sort()
    res = []

    def dp(target, route, i):
        if target == 0:
            res.append(route)
            return route
        if i >= len(candidates):
            return False
        if candidates[i] > target:
            return False
        dp(target - candidates[i], route + [candidates[i]], i)
        dp(target, route, i + 1)

    dp(target, [], 0)
    return res

# O(2^target)
def how_sum_backtracking(candidates, target):
    res = []

    def dp(total, route, i):
        if total == target:
            res.append(route.copy())
            return
        if i >= len(candidates) or total > target:
            return

        route.append(candidates[i])
        dp(total + candidates[i], route, i)
        route.pop()
        dp(total, route, i + 1)

    dp(0, [], 0)
    return res


if __name__ == "__main__":
    print(how_sum([1,2,3,4], 100))
