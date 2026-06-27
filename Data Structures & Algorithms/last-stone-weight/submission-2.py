class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, n in enumerate(stones):
            stones[i] = -n
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -(heapq.heappop(stones))
            y = -(heapq.heappop(stones))

            if x > y:
                x = x - y
                heapq.heappush(stones, -x)
        if len(stones) == 1:
            return -(stones[0])
        else:
            return 0