class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        n = len(s)

        for i in range(n):
            temp = s[i]
            for j in range(i + 1, n):
                if s[j] not in temp:
                    temp += s[j]
                else:
                    break

            print(temp)

            maxL = max(len(temp), maxL)

        return maxL