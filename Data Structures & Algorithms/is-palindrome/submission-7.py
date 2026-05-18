class Solution:
    def isPalindrome(self, s: str) -> bool:
        sNew = ""

        for c in s:
            if c.isalnum():
                sNew += c.lower()

        return sNew == sNew[::-1]