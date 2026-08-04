class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            if int(i[11]+i[12])>60:
                c+=1
        return c