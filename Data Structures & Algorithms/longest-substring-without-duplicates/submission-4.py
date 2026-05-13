class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_l = 1
        longest_s = ""
        n = len(s)

        for i in range(n):
            longest_s = s[i]
            for j in range(i + 1, n):
                if s[j] not in longest_s:
                    longest_s += s[j]
                else:
                    max_l = max(max_l, len(longest_s))
                    print("MAX", max_l)
                    break
                
                max_l = max(max_l, len(longest_s))

        return max_l
