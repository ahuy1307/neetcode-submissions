import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {} # val - count

        for num in nums:
            dictionary[num] = 1 + dictionary.get(num, 0)

        
        heap = []

        for key in dictionary.keys():
            heapq.heappush(heap, (dictionary[key], key))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for h in heap:
            res.append(h[1])

        return res