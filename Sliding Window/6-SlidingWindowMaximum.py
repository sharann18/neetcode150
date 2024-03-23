#TC: O(n)
#SC: O(n)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        res = []

        left = right = 0
        dq = deque() #store indices

        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)

            if left > dq[0]:
                dq.popleft()

            if (right - left + 1) == k:
                res.append(nums[dq[0]])
                left += 1
            
            right += 1

        return res