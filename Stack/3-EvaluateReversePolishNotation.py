#TC: O(n)
#SC: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for ch in tokens:
            if ch == '+' or ch == '-' or ch == '*' or ch == '/':
                op2 = stack[-1]
                stack.pop()
                op1 = stack[-1]
                stack.pop()

                if ch == '+':
                    temp = op1 + op2
                elif ch == '-':
                    temp = op1 - op2
                elif ch == '*':
                    temp = op1 * op2
                else:
                    temp = int(op1 / op2)
                
                stack.append(temp)

            else:
                stack.append(int(ch))
        
        return stack[-1]