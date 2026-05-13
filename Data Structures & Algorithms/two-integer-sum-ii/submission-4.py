class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {}

        for index, num in enumerate(numbers):
            diff = target - num

            if diff in dictionary:
                return [dictionary[diff] + 1, index + 1]

            dictionary[num] = index