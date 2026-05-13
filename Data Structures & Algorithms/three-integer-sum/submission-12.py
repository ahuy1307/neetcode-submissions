class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for index, num in enumerate(nums):
            if num > 0:
                break

            if index > 0 and nums[index - 1] == nums[index]:
                continue

            l, r = index + 1, n - 1

            while l < r:
                sumT = num + nums[l] + nums[r]

                if sumT > 0:
                    r -= 1
                elif sumT < 0:
                    l += 1 
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
            
        return res