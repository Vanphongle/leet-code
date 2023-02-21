class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat:
            return []
        
        rows, cols = len(mat), len(mat[0])
        max_dist = rows + cols
        
        # Traverse matrix from top-left to bottom-right
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    continue
                
                # Check distance to left and top cells
                left_dist = mat[i][j-1] if j > 0 else max_dist
                top_dist = mat[i-1][j] if i > 0 else max_dist
                
                # Update distance to nearest zero for current cell
                mat[i][j] = min(left_dist, top_dist) + 1
        
        # Traverse matrix from bottom-right to top-left
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if mat[i][j] == 0:
                    continue
                
                # Check distance to right and bottom cells
                right_dist = mat[i][j+1] if j < cols-1 else max_dist
                bottom_dist = mat[i+1][j] if i < rows-1 else max_dist
                
                # Update distance to nearest zero for current cell
                mat[i][j] = min(mat[i][j], min(right_dist, bottom_dist) + 1)
        
        return mat
