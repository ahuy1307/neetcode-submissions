class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        left = 0

        while left + len_s1 - 1 < len_s2:
            temp = s2[left: left + len_s1]

            if sorted(temp) == sorted(s1):
                return True

            left +=1

        return False