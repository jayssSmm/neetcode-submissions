class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''for i in range(len(numbers)):
            req = target - numbers[i]
            req_index=0
            l = 0
            h = len(numbers)-1
            while (l<=h):
                mid = int((h+l)/2)
                if numbers[mid]==req:
                    print(numbers[mid], req)
                    req_index = mid
                    break
                elif numbers[mid]<req:
                    l=mid+1
                elif numbers[mid]>req:
                    h=mid-1

            return [i+1, req_index+1]'''

        i = 0
        j = len(numbers)-1
        while (i<=j):
            if numbers[i]+numbers[j]==target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1