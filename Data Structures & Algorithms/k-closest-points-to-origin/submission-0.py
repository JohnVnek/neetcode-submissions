class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            dist = (x-0)**2 + (y-0)**2
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res