class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        for i in range(n2 - n1 + 1):
            print(i)
            if sorted(s1) == sorted(s2[i:i+n1]):
                return True

        return False