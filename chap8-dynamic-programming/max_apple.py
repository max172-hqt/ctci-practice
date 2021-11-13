# ----- Find a recursive solution -----
# When encountering a tree, 
# - we either pick apples from that tree
#   - need to skip the next tree (i-2)
# - or skip the tree (i-1)
# recursively find the min remaining apple (for the no. apple to be maxxed out)
# out of those two choices

# def get_max_number_of_apples_rec(arr, max):
#     def rec(rem, i):
#         if i < 0:
#             # No more tree left to pick apples
#             return rem
#         elif max < rem:
#             # Unable to pick apples from any tree because we are not allowed to
#             return rem
#         elif rem < arr[i]:
#             # Skip the tree because there're too many apples on that tree
#             return rec(rem, i-1)
#         # find min remaining apples from two choices above
#         return min(rec(rem-arr[i], i-2), rec(rem, i-1))
#     return max - rec(max, len(arr) - 1)

# ----- Solution with top-down approach -----
def get_max_number_of_apples(path):
    with open(path) as f:
        num_trees, max = [int(i) for i in f.readline().split()]
        # cut off trees whose index > num_trees - 1
        arr = [int(i) for i in f.readline().split()[:num_trees]]
    memo = {}
    return max - dp(arr, max, max, len(arr)-1, memo)

def dp(arr, max, rem, i, memo):
    key = f"{str(rem)}:{i}"
    if key in memo:
        return memo[key]
    elif i < 0 or max < rem:
        return rem
    elif rem < arr[i]:
        res = dp(arr, max, rem, i-1, memo)
    else:
        res = min(dp(arr, max, rem-arr[i], i-2, memo), dp(arr, max, rem, i-1, memo))
    memo[key] = res
    return res

def get_max_test(arr, max):
    memo = {}
    return max - dp(arr, max, max, len(arr)-1, memo)

def test():
    # empty array
    assert get_max_test([], 100) == 0
    # max less than all trees
    assert get_max_test([1,2,3,4], 0) == 0
    # test sample case
    assert get_max_test([50,10,20,30,40], 100) == 90
    # test same apple numbers
    assert get_max_test([40,10,40,30,10], 100) == 90
    assert get_max_test([1,1,1,1,1,1], 100) == 3
    assert get_max_test([1,2,1,1,1,1], 100) == 4
    assert get_max_test([2,1,1,2,1,1], 3) == 3
    assert get_max_test([2,1,1,2,1,1], 4) == 4
    assert get_max_test([2,1,1,2,1,1], 5) == 5

if __name__ == "__main__":
    test()
    print(get_max_number_of_apples("./test.txt"))
