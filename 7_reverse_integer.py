class Solution:
    def reverse(self, x: int) -> int:
        INT32_MIN, INT32_MAX = -2**31, 2**31 - 1
        result = 0
        is_negative = x < 0
        x = abs(x)

        while x != 0:
            pop = x % 10
            x //= 10

            if result > (INT32_MAX - pop) // 10:
                return 0

            result = result * 10 + pop

        return -result if is_negative else result

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))
