class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for i, n in enumerate(nums):
            heapq.heappush(minHeap, n)
            if i > 0 and len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]