class Solution(object):
    def countHomogenous(self, s):
        MOD = 10**9 + 7
        count = 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result = (result + count * (count + 1) // 2) % MOD
                count = 1

        result = (result + count * (count + 1) // 2) % MOD

        return result
