class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        default = defaultdict(list)

        for i in range(len(strs)):
            default["".join(sorted(strs[i]))].append(strs[i])

        return list(default.values())