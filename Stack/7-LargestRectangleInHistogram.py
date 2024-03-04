#TC: O(n)
#SC: O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = deque()

        for i, height in enumerate(heights):
            startIdx = i
            
            while stack and height < stack[-1][1]:
                poppedIdx, poppedHeight = stack.pop()
                area = poppedHeight*(i - poppedIdx)
                maxArea = max(area, maxArea)
                startIdx = poppedIdx

            stack.append([startIdx, height])
        
        for i, height in stack:
            area = height*(len(heights) - i)
            maxArea = max(area, maxArea)

        return maxArea