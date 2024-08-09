"""
from heapq import heappop, heappush
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        min_heap = []

        for x, y in points:
            while min_heap and x - min_heap[0][1] > k:
                heappop(min_heap)

            if min_heap:
                max_value = max(max_value, min_heap[0][0] + x + y)

            heappush(min_heap, (y - x, x))

        return max_value
        
        """
        
from math import inf
class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        res = -inf
        i = 0
        n = len(points)
        last = 0

        while i < n:
            if i >= last:
                last = i + 1

            for j in range(last, n):
                if points[j][0] > k + points[i][0]:
                    break
                else:
                    tp = points[i][1] + points[j][1] + points[j][0] - points[i][0]
                    if tp > res:
                        res = tp
                        last = j
            i += 1
        return res
