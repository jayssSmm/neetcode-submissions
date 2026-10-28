class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        while l < len(nums):
            if nums[l] == 0:
                while r <= l or nums[r] == 0:
                    r+=1
                    if r == len(nums):
                        return
                nums[r], nums[l] = nums[l], nums[r]
            l+=1