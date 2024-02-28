#TC: O(n^2)
#SC: O(1) or O(n) depending upon the sorting algorithm
 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                if num + nums[left] + nums[right] == 0:
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        
        return output