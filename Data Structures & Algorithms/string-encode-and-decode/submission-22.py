class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        l = 0

        result = []

        while l < len(s):
            r = l + 1

            while s[r] != "#":
                r += 1

            length = int(s[l:r])
            r += 1
            l = r
            r += length

            result.append(s[l:r])
            l = r

        return result