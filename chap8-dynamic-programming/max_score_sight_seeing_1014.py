def max_score_sight_seeing_pair(values):
    max_src = values[0]
    best = 0
    for i in range(1, len(values)):
        best = max(best, values[i] + max_src - 1)
        # As we move further, we have to subtract the max_src place by 1
        # compare the value with the nearest location, to see if its worth
        # visiting the original src anymore
        max_src = max(max_src - 1, values[i])
    return best

    
    # prev = values[0] + 0
    # best = 0
    # max (values[i] + i -> (prev) + values[j] - j -> (curr)) 
    # for i in range(1, len(values)):
    #     best = max(best, prev + values[i] - i)
    #     prev = max(prev, values[i] + i)
        
    # return best


if __name__ == "__main__":
    print(max_score_sight_seeing_pair([8,1,5,2,6]))