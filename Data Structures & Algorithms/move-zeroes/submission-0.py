class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index, i in enumerate(nums):
            if not i:
                j = index+1
                while j < len(nums)-1 and nums[j]==0:
                    j+=1
                    if j == len(nums)-1:
                        break
                if j < len(nums):
                    nums[index], nums[j] = nums[j], nums[index]