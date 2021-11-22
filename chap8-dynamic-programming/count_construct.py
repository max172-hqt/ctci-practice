# return the number of ways that the target
# can be constructed by concatenating elements in
# the word_bank array
# m: target.length
# n: word_bank.length
# Time: O(n*m^2)
# Space: O(m^2)

def count_construct(target, word_bank):
    memo = {}
    def dp(target, memo):
        if target in memo: return memo[target]
        if target == "": return 1

        res = 0
        for word in word_bank:
            if target.startswith(word):
                suffix = target[len(word):]
                res += dp(suffix, memo)

        memo[target] = res
        return res
    return dp(target, memo)


if __name__ == '__main__':
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "cdef"]))
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(count_construct("eeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eee",
        "eeee",
        "eeeee",
        "eeeeee",
    ]))
    