class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num - 1 in nums:
                continue

            length = 1
            while num + 1 in nums:
                length += 1 
                num += 1

            res = max(res, length)

        return res