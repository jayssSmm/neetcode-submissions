class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0

        for i in s:
            if i-1 in s:
                pass
            else:
                lenght=1
                while (i + lenght) in s:
                    lenght+=1
                
                longest=max(longest, lenght)

        return longest