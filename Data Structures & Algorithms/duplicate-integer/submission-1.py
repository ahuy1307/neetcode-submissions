class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # l = len(nums)

        # for i in range(l):
        #     for j in range(i + 1, l, 1):
        #         if nums[j] == nums[i]:
        #             return True

        # return False

        new_set = set()

        for num in nums:
            if num in new_set:
                return True
            new_set.add(num)

        return False
        