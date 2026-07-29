class Solution:
    def minOperations(self, logs: List[str]) -> int:
        l = 0
        for i in logs:
            if i == "../":
                if l>0:
                    l-=1
            elif i == "./":
                pass
            else:
                l+=1
        return l