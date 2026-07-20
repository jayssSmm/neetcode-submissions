from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0

        i = 1
        j = max(piles)

        val = []
        while i<=j:
            k = (i+j)//2

            s=0
            for m in piles:
                s+=ceil(m/k)
            
            if s>h:
                i=k+1

            else:
                val.append(k)
                j=k-1

        return min(val)