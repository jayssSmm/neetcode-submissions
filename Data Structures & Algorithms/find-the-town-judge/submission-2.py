class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        to = dict()
        fro = dict()
        
        for i in trust:
            if i[0] in to:
                to[i[0]]+=1
            else:
                to[i[0]]=1

            if i[1] in fro:
                fro[i[1]]+=1
            else:
                fro[i[1]] = 1

        for i in fro:
            if fro[i] == n-1 and i not in to:
                return i

        return -1