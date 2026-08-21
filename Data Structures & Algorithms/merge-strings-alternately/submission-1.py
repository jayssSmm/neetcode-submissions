class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        x = []
        i = 0
        l1 = len(word1)
        l2 = len(word2)
        while True:
            x.append(word1[i])
            x.append(word2[i])
            if i == l1-1 or i == l2-1:
                break
            i+=1

        print(x, i)

        if l2 == l1:
            pass
        elif i == l1-1:
            x.extend(word2[i+1:])
        elif i == l2-1:
            x.extend(word1[i+1:])

        return ''.join(x)