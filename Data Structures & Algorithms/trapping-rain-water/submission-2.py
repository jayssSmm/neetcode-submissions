class Solution:
    def trap(self, height: List[int]) -> int:
        max1 = 0
        l1, l2 = [], []
        for i in height:
            if i > max1:
                max1 = i
            l1.append(max1)

        max1 = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > max1:
                max1 = height[i]
            l2.append(max1)

        l2.reverse()
        max1 = 0
        for i in range(len(height)):
            max1+= min(l1[i], l2[i]) - height[i]

        return max1