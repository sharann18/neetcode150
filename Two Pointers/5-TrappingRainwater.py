#TC: O(n)
#SC: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0

        while i < j:
            if height[i] <= height[j]:
                temp = i + 1
                while height[temp] < height[i]:
                    area += height[i] - height[temp]
                    temp += 1
                i = temp
                
            else:
                temp = j - 1
                while height[temp] < height[j]:
                    area += height[j] - height[temp]
                    temp -= 1
                j = temp
        
        return area