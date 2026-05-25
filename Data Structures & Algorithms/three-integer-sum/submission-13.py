class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []

        for index, num in enumerate(nums):
            if num > 0:
                break

            if index > 0 and num == nums[index - 1]:
                continue

            l = index + 1
            r = n - 1

            while l < r:
                sumT = nums[l] + nums[r] + num

                if sumT > 0:
                    r -= 1
                elif sumT < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], num])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res