class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for c in s:
            value = values[c]
            if value > prev_value:
                result -= 2 * prev_value
            result += value
            prev_value = value
        return result
