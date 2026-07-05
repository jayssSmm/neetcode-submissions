class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''d = {}
        count = 0
        for i, j in zip(s, t):
            d[i]=j
            if i in d.values():
                count+=1
        print(d)
        print(count)
        print(len(set(s)))
        if count == len(set(s)):
            return True
        return False'''
        return sorted(s) == sorted(t)