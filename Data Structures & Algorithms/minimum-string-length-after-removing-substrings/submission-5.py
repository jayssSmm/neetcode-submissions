class Solution:
    def minLength(self, s: str) -> int:
        x = []
        for i in s:
            if i == 'B' and x and x[-1] == 'A':
                    x.pop()
            elif i == 'D' and x and x[-1] == 'C':
                    x.pop()
            else:
                x.append(i)

        return len(x)