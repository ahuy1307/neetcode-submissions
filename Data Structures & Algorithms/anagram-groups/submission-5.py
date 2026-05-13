class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            dictionary[sortedS].append(s)

        return list(dictionary.values())