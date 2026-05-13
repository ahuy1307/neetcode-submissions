class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]

        temp = [1] * n
        for i in range(n - 2, -1, -1):
            temp[i] = nums[i + 1] * temp[i + 1]
            res[i] *= temp[i]

        return res