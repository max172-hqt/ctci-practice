def count_way_steps(n):
    if n == 1 or n == 2:
        return n
    a = 1
    b = 2
    for i in range(3, n):
        c = a + b
        a = b
        b = c
    return a + b


def count_triple_step(n):
    memo = [0] * (n + 1)

    def dp(n, memo):
        if n == 0:
            return 1
        if memo[n] == 0:
            for i in [1,2,3]:
                if n - i >= 0:
                    memo[n] += dp(n-i,memo)
        return memo[n]

    return dp(n, memo)


def count_triple_step_bottom_up(n):
    if n == 0: return 1
    memo = [0] * (n + 1)
    memo[0] = 1
    for i in range(1, n+1):
        total = 0
        for j in [1,2,3]:
            if i - j >= 0:
                total += memo[i - j]
        memo[i] = total
    return memo[n]


if __name__ == "__main__":
    print(count_way_steps(3))
    print(count_triple_step(6))
    print(count_triple_step_bottom_up(6))
