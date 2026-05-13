class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for k in s:
            if k.isalnum():
                new_str += k.lower()
        
        return new_str == new_str[::-1]