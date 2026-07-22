class Solution:
    def isValid(self, s: str) -> bool:
        bs = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s: 
            if c in bs:
                if stack and stack[-1] == bs[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)

        return True if not stack else False