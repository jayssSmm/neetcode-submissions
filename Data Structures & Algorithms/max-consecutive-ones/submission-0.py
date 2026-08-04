class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        m = 0
        for i in nums:
            if i:
                c+=1
            else:
                if c>m:
                    m=c
                c=0
        return m if m>c else c
            