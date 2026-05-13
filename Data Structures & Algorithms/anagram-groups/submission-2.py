class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        default = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            default[sortedS].append(s)

        res = []
        for d in default.values():
            res.append(d)

        return res