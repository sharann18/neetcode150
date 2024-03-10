#TC: O(26.n) which is O(n)
#SC: O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        maxLen = 0
        left, right = 0, 0

        counts = [0] * 26 #list to store the counts
       
        for right in range(0, len(s)):
            counts[ord(s[right]) - ord('A')] += 1
            winLen = right - left + 1

            if (winLen - max(counts)) <= k:
                maxLen = max(maxLen, winLen)

            else:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            
        
        return maxLen