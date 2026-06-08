class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        n = len(s)
        res = 0

        while l < n:
            r = l + 1
            length = s[l]

            while r < n and s[r] not in length:
                length += s[r]
                r += 1

            res = max(len(length), res)
            l += 1

        return res