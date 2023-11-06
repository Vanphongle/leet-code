class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor, temp_quotient = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                temp_quotient <<= 1
            dividend -= temp_divisor
            quotient += temp_quotient
        
        return -quotient if negative else quotient
