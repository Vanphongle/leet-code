class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate_helper(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                generate_helper(s + "(", left + 1, right)
            if right < left:
                generate_helper(s + ")", left, right + 1)
        
        result = []
        generate_helper("", 0, 0)
        return result
