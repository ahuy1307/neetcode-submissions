class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        heap = []

        for key in count.keys():
            heapq.heappush(heap, (count[key], key))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for h in heap:
            result.append(h[1])

        return result
