class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid),len(grid[0])
        p = 0
        seen = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c):
            nonlocal p
            if (r,c) in seen:
                return
            if (
                r < 0 or r >= row
                or c < 0 or c>= col
                or grid[r][c] == 0
            ):
                p+=1
                return
                
            seen.add((r,c))
            for sr,sc in directions:
                dfs(sr + r,sc + c)
            
        for r in range(row):
            for c in range(col):
                if (
                    (r,c) not in seen
                    and grid[r][c] == 1
                    ):
                    dfs(r,c)
        return p


            
        