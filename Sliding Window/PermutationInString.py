#TC: O(n)
#SC: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26

        left, right = 0, 0

        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1

        while right < len(s2):

            while (right - left + 1) != len(s1):
                counts2[ord(s2[right]) - ord('a')] += 1
                right += 1

            counts2[ord(s2[right]) - ord('a')] += 1
            
            if counts1 == counts2:
                return True
            
            counts2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1

        return False