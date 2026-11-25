class Solution:
    def minLength(self, s: str) -> int:
        x = [s[0]]
        for i in range(1, len(s)):
            if s[i] == 'B' and x and x[-1] == 'A':
                    x.pop()
            elif s[i] == 'D' and x and x[-1] == 'C':
                    x.pop()
            else:
                x.append(s[i])

        return len(x)