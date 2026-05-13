class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n, 1):
                if nums[j] + nums[i] == target:
                    return [i, j]