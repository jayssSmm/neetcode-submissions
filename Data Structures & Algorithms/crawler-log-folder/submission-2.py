class Solution:
    def minOperations(self, logs: List[str]) -> int:
        l = []
        for i in logs:
            if i == "../":
                if len(l)!=0:
                    l.pop()
            elif i == "./":
                pass
            else:
                l.append(i)
        return len(l)