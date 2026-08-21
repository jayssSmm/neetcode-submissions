class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        x = []
        i = 0
        while True:
            x.append(word1[i])
            x.append(word2[i])
            if i == len(word1)-1 or i == len(word2)-1:
                break
            i+=1

        print(x, i)

        if len(word2) == len(word1):
            pass
        elif i == len(word1)-1:
            x.extend(word2[i+1:])
        elif i == len(word2)-1:
            x.extend(word1[i+1:])

        return ''.join(x)