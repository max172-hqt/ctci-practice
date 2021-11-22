# def deleteAndEarn(nums):
#     table = {}
#     for num in nums:
#         if num not in table:
#             table[num] = num
#         else:
#             table[num] += num
    
#     memo = {}
#     def brute(curr, deleted, memo):
#         remaning_keys = [key for key in table.keys() if key not in deleted]
#         memo_key = f"{curr}-{'-'.join([str(num) for num in sorted( remaning_keys )])}"
#         if memo_key in memo:
#             print(memo_key, memo[memo_key])
#             return memo[memo_key]
#         if set(table.keys()).issubset(set(deleted)):
#             return curr
#         max_points = 0
#         for key in remaning_keys:
#             deleted.append(key+1)
#             deleted.append(key-1)
#             deleted.append(key)
#             new_points = brute(curr + table[key], deleted, memo)
#             memo[memo_key] = new_points
#             if (new_points > max_points):
#                 max_points = new_points
#             deleted.pop()
#             deleted.pop()
#             deleted.pop()
        
#         return max_points
            
#     return brute(0, [], memo)

# def deleteAndEarn(nums):
#     table = {}
#     for num in nums:
#         if num not in table:
#             table[num] = num
#         else:
#             table[num] += num 

#     n = max(table.keys())
#     houses = [0] * (n + 1)
#     for i in range(n + 1):
#         if i in table:
#             houses[i] = table[i]
#     print(houses)
#     a = houses[0]
#     b = max(houses[0], houses[1])
#     for i in range(2, len(houses)):
#         c = max(a + houses[i], b)
#         a = b
#         b = c
#     return b

from collections import Counter

def deleteAndEarn(nums):
    counter = Counter(nums)
    avoid = 0  # Not using prev
    using = 0  # Using prev
    prev = -1
    
    for k in sorted(counter):
        if k - 1 == prev:
            avoid, using = max(using, avoid), k * counter[k] + avoid
        else:
            avoid, using = max(using, avoid), k * counter[k] + max(using, avoid)
        prev = k
    
    return max(avoid, using)
    
if __name__ == '__main__':
    test = [2,2,3,3,3,4]

    print(deleteAndEarn(test))