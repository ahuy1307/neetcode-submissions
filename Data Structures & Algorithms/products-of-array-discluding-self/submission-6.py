class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [1] * n
        res = temp

        for i in range(1, n):
            res[i] = nums[i - 1] * temp[i - 1]
            temp[i] = res[i]

        temp = [1] * n

        for i in range(n - 2, -1, -1):
            print(i)
            temp[i] = nums[i + 1] * temp[i + 1]
            res[i] = res[i] * temp[i]

        return res