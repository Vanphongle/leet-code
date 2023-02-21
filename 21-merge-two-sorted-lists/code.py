class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack to store the open brackets
        stack = []
        
        # Traverse the string
        for c in s:
            if c in ['(', '{', '[']:
                # If the current character is an open bracket, push it onto the stack
                stack.append(c)
            elif c in [')', '}', ']']:
                # If the current character is a close bracket, check if the stack is empty or if the top of the stack does not correspond to the current close bracket
                if not stack or (c == ')' and stack[-1] != '(') or (c == '}' and stack[-1] != '{') or (c == ']' and stack[-1] != '['):
                    return False
                else:
                    # If the top of the stack corresponds to the current close bracket, pop the top element from the stack
                    stack.pop()
        
        # If the traversal completes and the stack is not empty, return False. Otherwise, return True.
        return not stack
