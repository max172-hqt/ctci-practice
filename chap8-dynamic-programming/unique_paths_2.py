def unique_paths_with_obstacles(obstacle_grid) -> int:
    memo = {}
    m = len(obstacle_grid) - 1
    n = len(obstacle_grid[0]) - 1
    return dp(m, n, obstacle_grid, memo)


def dp(m, n, arr, memo):
    key = f"{m}:{n}"
    if key in memo:
        return memo[key]
    if m == 0 and n == 0:
        return 1 if arr[m][n] == 0 else 0
    if arr[m][n] == 1:
        return 0
    total = 0

    if m > 0 and arr[m-1][n] == 0:
        total += dp(m-1,n,arr,memo)
    if n > 0 and arr[m][n-1] == 0:
        total += dp(m,n-1,arr,memo)
    memo[key] = total
    return total

def unique_paths_with_obstacles_2(obstacle_grid) -> int:
    m = len(obstacle_grid)
    n = len(obstacle_grid[0])

    if obstacle_grid[0][0] == 1:
        return 0

    obstacle_grid[0][0] = 1

    for i in range(1,m):
        obstacle_grid[i][0] = int(obstacle_grid[i][0] == 0 and obstacle_grid[i-1][0] == 1)

    for j in range(1,n):
        obstacle_grid[0][j] = int(obstacle_grid[0][j] == 0 and obstacle_grid[0][j-1] == 1)

    for i in range(1,m):
        for j in range(1,n):
            if obstacle_grid[i][j] == 1:
                obstacle_grid[i][j] = 0
            else:
                obstacle_grid[i][j] = obstacle_grid[i-1][j] + obstacle_grid[i][j-1]

    return obstacle_grid[m-1][n-1]


if __name__ == "__main__":
    print(unique_paths_with_obstacles([[0,1],[0,0]]))
    print(unique_paths_with_obstacles_2([[0,1],[0,0]]))