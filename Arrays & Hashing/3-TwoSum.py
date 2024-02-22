#brute force
#TC: O(n^2)
#SC: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#using hashmap
#TC: O(n)
#SC: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i, hashmap[diff]]
            
            hashmap[n] = i
        
        return