class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        # Initialize the result with the first row
        result = [[1]]
        
        for i in range(1, numRows):
            # Calculate the next row based on the previous row
            prev_row = result[-1]
            new_row = [1]  # First element is always 1
            
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j - 1] + prev_row[j])  # Sum of two elements above
                
            new_row.append(1)  # Last element is always 1
            result.append(new_row)
        
        return result
