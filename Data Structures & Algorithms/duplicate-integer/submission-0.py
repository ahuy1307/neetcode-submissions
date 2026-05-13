class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)

        for i in range(l):
            for j in range(i + 1, l, 1):
                if nums[j] == nums[i]:
                    return True

        return False
        