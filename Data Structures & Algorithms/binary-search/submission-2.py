class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums)-1
        l = 0

        while l<=h:
            mid = int((h+l)/2)
            print(mid)
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                h=mid-1;
            else:
                break
        if nums[mid]==target:
            return mid
        return -1