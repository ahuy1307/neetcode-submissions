class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            new_set = set()
            for j in range(i, n):
                if s[j] in new_set:
                    break
                
                new_set.add(s[j])

            res = max(res, len(new_set))

        return res