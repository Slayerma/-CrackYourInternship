from collections import defaultdict
class Solution:

    def subarraySum(self, nums: list[int], k: int) -> int:

        count = 0
        prefix_sum = 0
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1
        for num in nums:
            prefix_sum += num
            count += prefix_sum_counts[prefix_sum - k]
            prefix_sum_counts[prefix_sum] += 1
        return count
