def can_construct(target, word_bank):
    memo = {}
    def dp(target, memo):
        if target in memo:
            return memo[target]
        if target == "":
            return True
        for word in word_bank:
            if target.startswith(word):
                suffix = target[len(word):]
                if dp(suffix, memo):
                    memo[target] = True
                    return True
        memo[target] = False
        return False
    return dp(target, memo)

# m = target.length
# n = word_bank.length
# O(n * m^2) 1 m is for slice
# O(m^2) space

if __name__ == '__main__':
    print(can_construct("abcdef", ["abc", "ab", "def", "de"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eee",
        "eeee",
        "eeeee",
        "eeeeee",
    ]))