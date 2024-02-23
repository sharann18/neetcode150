#Using hashmap
#TC: O(n^2)
#SC: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        for i in range(0,k):
            max_count = max(count.values())
            
            elt = [key for key in count if count[key] == max_count]
            
            freq.extend(elt)

            if len(freq) == k:
                break
        
            for x in elt:
                count.pop(x)
            
        return freq

#Using hashmap + modified bucket sort
#TC: O(n)
#SC: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = {}
        res = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1, 0, -1):
            if freq[i] != []:
                res.extend(freq[i])
            
            if len(res) == k:
                return res
        
        return res