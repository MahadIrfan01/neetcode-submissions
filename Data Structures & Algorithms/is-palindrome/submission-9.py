class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 

        while l < r:
            if not s[l].isalnum(): 
                l+=1
                continue
            elif not s[r].isalnum():
                r-=1
                continue
            if s[r].upper() == s[l].upper():
                l+=1
                r-=1
            elif s[r].upper() != s[l].upper():
                return False
        return True 
            