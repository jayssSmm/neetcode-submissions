class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 1:
            return 0
        y = abs(ord(s[0]) - ord(s[1]))
        for i in range(2, len(s)):
            y+=abs(ord(s[i]) - ord(s[i-1]))

        return y