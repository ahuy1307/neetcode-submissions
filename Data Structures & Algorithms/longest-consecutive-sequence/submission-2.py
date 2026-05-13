class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0

        for nums in set_nums:
            length = 1
            while nums - 1 in set_nums:
                length += 1
                nums -= 1

            res = max(res, length)

        return res