'''
https://leetcode.com/problems/flood-fill/submissions/1008744613/
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        n = len(image)
        m = len(image[0])
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            if image[r][c] == start_color and image[r][c] != color:
                image[r][c] = color
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        dfs(sr,sc)
        return image
            