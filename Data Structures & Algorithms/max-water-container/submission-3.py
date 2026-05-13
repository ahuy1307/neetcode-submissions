class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        l = len(heights)

        for i in range(l):
            for j in range(i + 1, l):
                minL = min(heights[j], heights[i])
                maxA = max(maxA, minL * (j - i))

        return maxA