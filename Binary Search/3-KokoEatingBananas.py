#TC: O(log(max(p))*p)
#SC: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minSpeed = max(piles)

        while left <= right:
            hours = 0
            mid = (left + right) // 2

            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours <= h:
                minSpeed = min(mid, minSpeed)
                right = mid - 1
            else:
                left = mid + 1
            
        return minSpeed