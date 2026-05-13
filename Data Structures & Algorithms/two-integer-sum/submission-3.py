class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        default = defaultdict(int)
        n = len(nums)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in default:
                return [default[diff], i]
            
            default[num] = i