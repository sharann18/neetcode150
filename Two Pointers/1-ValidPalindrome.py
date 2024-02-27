#Using reverse iteration
#TC: O(n)
#SC: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""

        for ch in s:
            if ch.isalnum():
                s2 += ch.lower()
        
        return s2 == s2[::-1]
    
#Using two pointers and ascii codes (memory optimization)
#TC: O(n)
#SC: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            while left < right and not self.isAlphNum(s[left]):
                left += 1

            while right > left and not self.isAlphNum(s[right]):
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True


    def isAlphNum(self, ch: str) -> bool:
        return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9'))