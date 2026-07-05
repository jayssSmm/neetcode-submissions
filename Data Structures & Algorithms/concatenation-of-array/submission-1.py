class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = nums.copy()
        for i in nums:
            l.append(i)

        return l