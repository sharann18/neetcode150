#Monotonic Stack (decreasing)
#TC: O(n)
#SC: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = deque() #pair of temp and indices

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackT, stackI = stack.pop()
                answer[stackI] = (i - stackI)
            
            stack.append([temp,i])
        
        return answer