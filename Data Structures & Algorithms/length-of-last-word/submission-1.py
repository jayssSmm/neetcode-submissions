class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = []
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            x.append(s[i])

        return len(x)