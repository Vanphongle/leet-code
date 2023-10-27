class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        i = 0

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if result > (2**31 - digit) // 10 or result == (2**31 - digit) // 10 and sign == 1 and digit > 7:
                return 2**31 - 1 if sign == 1 else -2**31

            result = result * 10 + digit
            i += 1

        result *= sign

        return result
