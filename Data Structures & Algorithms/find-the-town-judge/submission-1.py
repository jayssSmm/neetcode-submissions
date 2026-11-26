class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = dict()
        for i in range(1, n+1):
            d[i] = {"points to":0, "pointed by":0}

        for (to, fro) in trust:
            d[to]["points to"]+=1
            d[fro]["pointed by"]+=1

        for i in d:
            if d[i]['points to'] == 0 and d[i]['pointed by'] == n-1:
                return i

        return -1