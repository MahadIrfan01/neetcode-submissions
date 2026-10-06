class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = {}

        for n in nums: 
            res[n] = res.get(n, 0) + 1
        best = 0
        for n in nums: 
            counter =1
            if (n-1) in res:
                continue 
            while (n + 1) in res: 
                counter +=1
                n += 1
            best = max(best, counter)

        return best