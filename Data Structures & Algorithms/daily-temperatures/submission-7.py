class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting = [0]
        y = (temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures[waiting[-1]]:
                while waiting and temperatures[i] > temperatures[waiting[-1]]:
                    y[waiting[-1]] = (i-waiting[-1])
                    waiting.pop()
            waiting.append(i)

        
        for i in waiting:
            y[i] = 0

        return y