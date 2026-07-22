class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1, l2 = [], []

        for n in nums1:
            if n not in nums2 and n not in l1: 
                l1.append(n)

        for n in nums2:
            if n not in nums1 and n not in l2:
                l2.append(n)
        return [l1, l2]