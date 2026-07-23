class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        hs = {'+', '-', '/', '*'}

        for c in tokens:
            if c not in hs:
                stack.append(int(c))
            else:
                c1 = int(stack.pop())
                c2 = int(stack.pop())
                if c == '+':
                    stack.append((c1+c2))
                elif c == '-':
                    stack.append((c2-c1))
                elif c == '/':
                    stack.append(int(c2 / c1))
                else: 
                    stack.append(c1*c2)
        return stack[-1]
                

