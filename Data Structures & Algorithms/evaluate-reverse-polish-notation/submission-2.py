class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        

        hs = {'+', '/', '-', '*'}
        for i in range(len(tokens)):
            if tokens[i] not in hs: 
                stack.append(int(tokens[i]))
            else:
                str1=stack.pop()
                str2=stack.pop()
                if tokens[i] == '+':
                    stack.append((str1) + (str2))
                elif tokens[i] == '*':
                    stack.append((str1) * (str2))
                elif tokens[i] == '/':
                    stack.append(int((str2) / (str1)))
                else: 
                    stack.append((str2) - (str1))
                
        return stack[-1]


