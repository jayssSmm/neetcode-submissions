class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        waiting = [0]
        for i in range(1, len(prices)):
            if prices[i] <= prices[waiting[-1]]:
                while waiting and prices[i] <= prices[waiting[-1]]:
                    prices[waiting[-1]]-=prices[i]
                    waiting.pop()
            waiting.append(i)

        return prices