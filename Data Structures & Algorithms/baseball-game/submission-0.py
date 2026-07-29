class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for i in operations:
            if i == '+':
                l.append(l[len(l)-1]+l[len(l)-2])
            elif i == 'C':
                l.pop()
            elif i == 'D':
                l.append(l[len(l)-1]*2)
            else:
                l.append(int(i))

        return sum(l)