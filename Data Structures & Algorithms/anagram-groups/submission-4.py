class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        default = defaultdict(list)
        
        for s in strs:
            sortedS = "".join(sorted(s))
            default[sortedS].append(s)

        return list(default.values())