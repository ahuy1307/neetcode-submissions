class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        res = 1
        n = len(s)

        for i in range(n):
            long_s = s[i]
            for j in range(i + 1, n):
                if s[j] in long_s:
                    break
                else:
                    long_s += s[j]

            res = max(len(long_s), res)

        return res