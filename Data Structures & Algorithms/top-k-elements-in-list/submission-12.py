class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # val - count

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for key in count.keys():
            heapq.heappush(heap, (count[key], key))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for h in heap:
            res.append(h[1])

        return res
