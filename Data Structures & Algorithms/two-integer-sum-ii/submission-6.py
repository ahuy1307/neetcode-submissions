class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sumT = numbers[l] + numbers[r]

            if sumT > target:
                r -= 1
            elif sumT < target:
                l +=1
            else:
                return [l + 1, r + 1]