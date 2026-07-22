class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        if len(s) != len(t): 
            return False

        for i in range(len(s)): 
            s1[s[i]] = s1.get(s[i], 0) + 1
            s2[t[i]] = s2.get(t[i], 0) + 1  
        return s1 == s2