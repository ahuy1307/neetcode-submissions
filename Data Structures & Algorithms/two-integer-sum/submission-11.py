class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {} # val - index
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]

            if diff in count:
                return [count[diff], i]

            count[nums[i]] = i

        