# def get_max_len(nums):
#     best_len = 0
#     sub_arrays = []
#     temp = []
#     for i, num in enumerate(nums):
#         if num == 0:
#             sub_arrays.append(temp.copy())
#             temp = []
#             continue
#         temp.append(num)
#         if i == len(nums) - 1:
#             sub_arrays.append(temp.copy())
#     for arr in sub_arrays:
#         index_negative = [arr.index(num) for num in arr if num < 0]
#         if len(index_negative) % 2 == 0:
#             best_len = max(best_len, len(arr))
#         elif len(index_negative) == 1:
#             best_len = max(best_len, len(arr[:index_negative[0]]), len(arr[index_negative[0]:]) - 1)
#         else:
#             print(sub_arrays)
#             print(len(arr) - len(arr[:index_negative[0]+1]), 'dsad')
#             print(arr[index_negative[len(index_negative)-1]:])
#             print(index_negative)
#             print(len(arr) - len(arr[index_negative[len(index_negative)-1]:]), 'dsad')
#             best_len = max(best_len, len(arr) - len(arr[:index_negative[0]+1]), len(arr) - len(arr[index_negative[len(index_negative)-1]:]))
            
#     return best_len

def get_max_len(nums):
    best = 0
    i = 0
    while i < len(nums):
        s = i
        while s < len(nums) and nums[s] == 0: s += 1
        e = s

        while e < len(nums) and nums[e] != 0:
            count_negative = 0
            start_negative = -1
            end_negative = -1
            if nums[e] < 0:
                count_negative += 1
                if start_negative == -1:
                    start_negative = e
                end_negative = e
            e += 1

        if count_negative % 2 == 0:
            best = max(best, e - s)
        else:
            best = max(best, e - s - min(start_negative - s + 1, e - end_negative))
        i = e
    return best

if __name__ == "__main__":
    print(get_max_len([3,12,1,-2,-3,-2,-15,-15]))