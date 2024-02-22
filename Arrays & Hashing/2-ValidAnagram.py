#using hashmaps to count the occurences of characters and comparing them
#TC: O(s+t)
#SC: O(s+t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        #iterating through the key values
        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        
        return True

#sort both string and compare
#TC: O(nlogn)
#SC: O(1) assuming the sorting fn doesn't use extra memory
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)