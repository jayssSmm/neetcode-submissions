class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        p = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    pass
                else:
                    if i-1<0:
                        
                        p+=1
                    if i+1>=r:
                        
                        p+=1
                    if j+1>=c:
                        
                        p+=1
                    if j-1<0:
                        
                        p+=1

                    if i+1<r and grid[i+1][j] == 0:
                        
                        p+=1
                    if i-1>=0 and grid[i-1][j] == 0:
                        
                        p+=1

                    if j+1<c and grid[i][j+1] == 0:
                        
                        p+=1
                    if j-1>=0 and grid[i][j-1] == 0:
                        
                        p+=1
                    

        return p