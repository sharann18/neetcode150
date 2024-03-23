#TC: O(m*logn)
#SC: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(0, len(matrix)):
            left, right = 0, len(matrix[i]) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False

#TC: O(log(m*n))
#SC: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        
        while top <= bottom:
            row = (top + bottom) // 2

            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                break
        
        if top > bottom:
            return False

        row = (top + bottom) // 2

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False