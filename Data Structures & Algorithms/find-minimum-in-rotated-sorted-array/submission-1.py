class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return nums
        if len(nums)==1:
            return nums[0]

        l=0
        h=len(nums)-1

        while l<h:
            mid = (l+h)//2
            if nums[mid] > nums[h]:
                l=mid+1
            elif nums[mid] < nums[h]:
                h=mid

        return nums[l]