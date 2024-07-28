from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        total_sum = 0
        for num in nums:
            total_sum += num
            count += prefix_sum[(total_sum % k)]
            prefix_sum[(total_sum % k)] += 1
        return count
