class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)

        for i in nums:
            nums_dict[i]+=1

        sorted_dict_by_key = dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict_by_key)
    
        result = [0] * len(sorted_dict_by_key.keys())
        count = 0
        for i in sorted_dict_by_key.keys():
            print(count, i)
            result[count] = i
            count+=1

        return result[:k]