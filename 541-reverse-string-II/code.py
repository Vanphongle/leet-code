class Solution(object):
    def reverseStr(self, s, k):
        # Convert the string to a list of characters
        s = list(s)
        
        # Reverse the characters in every group of 2k characters
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        
        # Convert the list of characters back to a string and return it
        return ''.join(s)
