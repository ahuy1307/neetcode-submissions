class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, num in enumerate(nums):
            if num > 0: # array is sorted, so after this num always > 0
                break

            if index > 0 and nums[index - 1] == num:
                continue 

            l, r = index + 1, len(nums) - 1

            while l < r:
                sumThree = num + nums[l] + nums[r]

                if sumThree > 0:
                    r -=1
                elif sumThree < 0:
                    l +=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res


