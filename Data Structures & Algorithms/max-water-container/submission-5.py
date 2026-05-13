class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxT = 0

        while l < r:
            minT = min(heights[l], heights[r])
            maxT = max(maxT, minT * (r - l))

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        
        return maxT