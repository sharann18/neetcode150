#Using hashmap and stack
#TC: O(n)
#SC: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in closeToOpen:
                if stk and stk[-1] == closeToOpen[ch]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(ch)
        
        return True if not stk else False

#Using only stack
#TC: O(n)
#SC: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stk.append(ch)
            elif len(stk) > 0:
                if (ch == ')' and stk[-1] == '(') or (ch == ']' and stk[-1] == '[') or (ch == '}' and stk[-1] == '{'):
                    stk.pop()
                else:
                    return False
            else:
                return False

        return True if not stk else False