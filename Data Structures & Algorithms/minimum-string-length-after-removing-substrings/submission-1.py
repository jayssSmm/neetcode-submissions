class Solution:
    def minLength(self, s: str) -> int:
        x = [s[0]]
        for i in range(1, len(s)):
            #print(x)
            if s[i].upper() == 'B' and x and x[-1].upper() == 'A':
                #while s[i].upper() == 'B' and x and x[-1].upper() == 'A':
                    x.pop()
            elif s[i].upper() == 'D' and x and x[-1].upper() == 'C':
                #while s[i].upper() == 'D' and x and x[-1].upper() == 'C':
                    x.pop()
            else:
                x.append(s[i])

        #print(x)
        return len(x)