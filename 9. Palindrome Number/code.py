class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            s = str(x)
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-i-1]:
                    return False
            return True
