class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictN = defaultdict(int) # val - index

        for index, num in enumerate(numbers):
            diff = target - num

            if diff in dictN and diff != num:
                return [dictN[diff] + 1, index + 1]

            dictN[num] = index