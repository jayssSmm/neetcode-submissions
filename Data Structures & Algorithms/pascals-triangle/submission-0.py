class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def row(n):
            if n==1:
                return [1]
            r = row(n-1)
            x = []
            for index in range(len(r)):
                if index == 0:
                    x.append(1)
                    continue
                x.append(r[index]+r[index-1])
            x.append(1)

            return x

        x = []
        for i in range(1, numRows+1):
            x.append(row(i))

        return x