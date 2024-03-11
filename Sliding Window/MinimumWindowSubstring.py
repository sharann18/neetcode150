#TC: O(n)
#SC: O(1)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        res = [-1, -1]
        resLen = float(inf)
        countT, countWin = {}, {}

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        
        have = 0
        need = len(countT)

        left = 0

        for right in range(len(s)):
            ch = s[right]
            countWin[ch] = countWin.get(ch, 0) + 1

            if ch in countT and countWin[ch] == countT[ch]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                countWin[s[left]] -= 1

                if s[left] in countT and countWin[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1
        
        l, r = res

        return s[l:r+1] if resLen != float(inf) else ""