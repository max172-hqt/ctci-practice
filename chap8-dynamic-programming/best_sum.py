# best_sum(7, [5,4,3,7])

def best_sum(target, candidates):
    if target == 0:
        return []
    if target < 0:
        return None

    shortest = None
    for num in candidates:
        remainder = target - num
        curr = best_sum(remainder, candidates)
        if curr is not None:
            res = curr + [num] 
            if shortest is None or len(res) < len(shortest):
                shortest = res
    return shortest


if __name__ == "__main__":
    print(best_sum(100, [5,25]))
