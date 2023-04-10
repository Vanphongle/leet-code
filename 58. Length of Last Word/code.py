class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        last_space_index = s.rfind(' ')
        if last_space_index == -1:
            return len(s)
        else:
            return len(s) - last_space_index - 1
