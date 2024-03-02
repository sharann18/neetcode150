#TC: O(4^n/sqrt(n))
#SC: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = deque()
        res = []

        def backtracking(opening, closing):
            #base case
            if opening == closing == n:
                res.append("".join(stack))
                return
            
            if opening < n:
                stack.append('(')
                backtracking(opening + 1, closing)
                stack.pop()
            
            if closing < opening:
                stack.append(')')
                backtracking(opening, closing + 1)
                stack.pop()
            
        backtracking(0, 0)
        return res