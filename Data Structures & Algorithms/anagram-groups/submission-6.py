class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list) # sorted - values

        for s in strs:
            sortedS = "".join(sorted(s))
            count[sortedS].append(s)

        return list(count.values())