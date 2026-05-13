class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        default = defaultdict(int)
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in default:
                return [default[diff], i]

            default[nums[i]] = i