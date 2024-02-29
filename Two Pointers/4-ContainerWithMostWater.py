#TC: O(n)
#SC: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0

        while i < j:
            currArea = min(height[i], height[j])*(j-i)
            area = max(currArea, area)

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        return area