class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        x = 0
        while s[index] == " ":
            index -= 1
        for i in range(index, -1, -1):
            if s[i] == ' ':
                break
            x+=1

        return x