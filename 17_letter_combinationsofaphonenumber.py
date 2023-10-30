class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Define a mapping of digits to letters
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def generate_combinations(index, current):
            if index == len(digits):
                combinations.append(current)
                return

            digit = digits[index]
            letters = digit_map[digit]

            for letter in letters:
                generate_combinations(index + 1, current + letter)

        combinations = []
        generate_combinations(0, '')
        return combinations
