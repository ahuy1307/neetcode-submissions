class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res 

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []

        while l < len(s):
            r = l + 1

            while s[r] != "#":
                r += 1

            height = int(s[l:r])
            r += 1
            l = r
            r += height

            res.append(s[l:r])
            l = r

        return res

