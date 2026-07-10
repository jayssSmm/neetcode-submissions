class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd=1
        count=0
        for i in nums:
            if i!=0:
                prd*=i
            else:
                count+=1

        l=[]
        for i in nums:
            if i==0 and count==1:
                l.append(prd)
            elif count>0:
               l.append(0)
            else:
                l.append(prd//i)

        return l