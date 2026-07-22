class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        li=[]
        nums.sort()

        for index, i in enumerate(nums):
            l = index+1
            h = len(nums)-1
            while l<h:
                if nums[l] + nums[h] == -i:
                    if [nums[l], i ,nums[h]] not in li:
                       li.append([nums[l], i ,nums[h]])
                    l+=1
                    h-=1
                elif nums[l]+nums[h]>-i:
                    h-=1
                else:
                    l+=1


        return li  