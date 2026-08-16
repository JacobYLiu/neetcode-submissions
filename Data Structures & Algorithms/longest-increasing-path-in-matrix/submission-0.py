class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        Restate: 
        - Given a 2d matrix, we want to get the path of strictly increasing
        numbers, then return that path's length.
        
        Constraints and edge case
        - Zeroes are allowed! as problem stated greater than or equal to 0
        - No negatives
        - Will there be a matrix of no valid paths?
        - Will there be a matrix of all same numbers [2,2,2],[2,2,2],[2,2,2]]?
        - neighbors that are equal to current cell
        - only horizontal and vertical movements
        - empty grids?
        - is there strictly decreasing grid?

        Approach: 
        Using DFS to traverse the grid, starting with minimal value in the grid. 
        I think I could use min(grid).get() to get the cell and push into the stack?
        - but actually longer path could start from anywhere, because the min value 
        could be next to really big values and I would be stuck


        Step 1: 
        - I need a set to keep track of visited
        - I need to append the 
        Time Complexity would be O(mn)
        SC: O(mn)
        '''

        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r,c, prev): # we need to know the prev value
            if (r<0 or c<0 or r ==rows or c ==cols or matrix[r][c]<=prev):
                return 0
            
            if (r,c) in cache: 
                return cache[(r,c)]

            length = 1
            length = max(length, 1+ dfs(r+1, c, matrix[r][c]))
            length = max(length, 1+ dfs(r-1, c, matrix[r][c]))
            length = max(length, 1+ dfs(r, c+1, matrix[r][c]))
            length = max(length, 1+ dfs(r, c-1, matrix[r][c]))
            cache[(r,c)] = length        

            return length


        for r in range(rows): 
            for c in range(cols): 
                dfs(r,c,-1)
        
        return max(cache.values())
