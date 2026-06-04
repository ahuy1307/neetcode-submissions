class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num - 1 in nums:
                continue

            height = 1
            while num + 1 in nums:
                height += 1
                num += 1

            res = max(height, res)

        return res
