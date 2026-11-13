class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 1:
            return 0
        y = 0
        for i in range(1, len(s)):
            y+=abs(ord(s[i]) - ord(s[i-1]))

        return y