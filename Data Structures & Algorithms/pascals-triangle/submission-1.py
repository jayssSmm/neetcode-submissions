class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = []
        for i in range(1, numRows+1):
            x = [1]*i
            for j in range(1, i-1):
                x[j] = r[i-2][j-1] + r[i-2][j]
            r.append(x)

        return r