class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        l=[]

        nums.sort()
        print(nums)

        count = 1

        for index, i in enumerate(nums):
            if index>0 and nums[index-1]==i-1:
                count+=1
            elif nums[index-1]==i:
                pass
            else:
                l.append(count)
                count = 1
        l.append(count)

        return max(l)
