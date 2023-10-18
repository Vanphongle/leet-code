class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_title = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            char = chr(columnNumber % 26 + ord('A'))
            column_title = char + column_title
            columnNumber = columnNumber // 26
        
        return column_title
