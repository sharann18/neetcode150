#using a hashset to check if a list contains duplicates
#TC: O(n)
#SC: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for x in nums:
            if x in hashset:
                return True
            
            hashset.add(x)
        
        return False