#Monotonic Stack (strictly increasing)
#TC: O(n)
#SC: O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        stack = []

        for pos, sp in sorted(pos_speed)[::-1]:
            time_taken = (target - pos)/sp

            if stack and stack[-1][1] >= time_taken:
                continue

            stack.append([pos, time_taken]) 
        
        return len(stack)