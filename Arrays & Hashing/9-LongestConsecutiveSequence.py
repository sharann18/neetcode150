#TC: O(n)
#SC: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxcount = 0
        
        for num in nums:
            count = 0
            if (num - 1) not in nums_set:
                count = 1
                nextnum = num + 1
                while nextnum in nums_set:
                    count += 1
                    nextnum += 1
            
            maxcount = max(maxcount,count)
        
        return maxcount