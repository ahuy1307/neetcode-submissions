class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set()
        n = len(nums)

        for i in range(n):
            if nums[i] in new:
                return True
            new.add(nums[i])

        return False