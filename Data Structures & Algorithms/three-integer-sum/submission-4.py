class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dictN = defaultdict(int) # val - count

        for num in nums:
            dictN[num] +=1

        print(dictN)

        n = len(nums)
        res = defaultdict(list)

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                minus = 0 - nums[i] - nums[j]
                if nums[i] != nums[j]:
                    t = dictN[nums[i]] - 1
                    k = dictN[nums[j]] - 1
                else:
                    t = k = dictN[nums[i]] - 2

                if minus in dictN:
                    if minus in (nums[i], nums[j]) and (t == 0 or k == 0):
                        continue 

                    res["".join((str(x) for x in sorted([nums[i], nums[j], minus])))] = [nums[i], nums[j], minus]

        new = []

        for val in res.values():
            new.append(val)

        return new