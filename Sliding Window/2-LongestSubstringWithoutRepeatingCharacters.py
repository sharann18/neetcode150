#TC: O(n)
#SC: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i = 0
        maxLength = 1
        seen = set()

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxLength = max(maxLength, j - i + 1)

        return maxLength