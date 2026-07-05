class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            l=0
            h=len(matrix[i])-1
            while(l<=h):
                mid=int((h+l)/2)
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    h=mid-1
                else:
                    l=mid+1
            

        return False