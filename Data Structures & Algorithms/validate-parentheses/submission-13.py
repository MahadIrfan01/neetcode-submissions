class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        seen = { ')' : '(', ']' : '[', '}' : '{'}

        for n in s: 
            if n in seen:
                if stack and stack[-1] == seen[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        
        return True if not stack else False