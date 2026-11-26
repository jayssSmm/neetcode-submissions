class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [(sr, sc)]
        r = len(image)
        c = len(image[0])
        visited = []
        src = image[sr][sc]

        while stack:
            x, y = stack.pop()
            if image[x][y] == src:
                image[x][y] = color
            visited.append((x, y))
            if x>0:
                if (x-1, y) not in visited and image[x-1][y] == src:
                    stack.append((x-1, y))
            if x<r-1:
                if (x+1, y) not in visited and image[x+1][y] == src:
                    stack.append((x+1, y))
            if y>0:
                if (x, y-1) not in visited and image[x][y-1] == src:
                    stack.append((x, y-1))
            if y<c-1:
                if (x, y+1) not in visited and image[x][y+1] == src:
                    stack.append((x, y+1))

        return image