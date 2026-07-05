import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l=[]
        for i in list(s):
            if i.lower() not in string.punctuation and not i.isspace():
                l.append(i.lower())

        print(l)
        for i in range(len(l)):
            if l[i]!=l[len(l)-1-i]:
                return False
        return True