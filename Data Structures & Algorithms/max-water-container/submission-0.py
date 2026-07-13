class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        h=len(heights)-1
        max=0
        while (l<=h):
            area = (h-l)*min(heights[h], heights[l])
            if area>max:
                max = area
            else:
                if heights[l]>heights[h]:
                    h-=1
                else:
                    l+=1

        return max