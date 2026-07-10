class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={']':'[', '}':'{', ')':'('}

        #91, 123, 40-41

        for i in s:
            if ord(i) in (91, 123, 40):
                l.append(i)
            elif i in d:
                try:
                    if d[i]!=l.pop():
                        return False
                except IndexError:
                    return False


        if len(l)==0:
            return True
        return False