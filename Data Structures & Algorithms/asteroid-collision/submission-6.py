class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            alive = True
            # collision only when top moves right and incoming moves left
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:      # top is smaller: it explodes, keep checking
                    stack.pop()
                elif stack[-1] == -a:   # equal: both explode
                    stack.pop()
                    alive = False
                else:                   # top is bigger: incoming explodes
                    alive = False
            if alive:
                stack.append(a)
        return stack