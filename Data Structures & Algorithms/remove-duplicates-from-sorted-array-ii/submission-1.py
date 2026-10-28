class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = dict()
        c = 0
        for index, i in enumerate(nums):
            if i not in d:
                c+=1
                d[i] = 1
            else:
                if d[i] == 1:
                    c+=1
                    d[i]+=1
                else:
                    nums[index] = None

        for index, i in enumerate(nums):
            if i == None:
                j = index+1
                while j < len(nums)-1 and nums[j]==None:
                    j+=1
                    if j == len(nums)-1:
                        break
                if j < len(nums):
                    nums[index], nums[j] = nums[j], nums[index]
        return c