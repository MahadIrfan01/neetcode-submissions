class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        seen = {')':'(', ']' : '[', '}' : '{'}
        for character in s:
            if character in seen: 
                if stack and stack[-1] == seen[character]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(character)
        return True if not stack else False