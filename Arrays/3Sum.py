class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                while j < k and nums[j] + nums[k] > -nums[i]:
                    k -= 1
                while j < k and nums[j] + nums[k] < -nums[i]:
                    j += 1
                if j < k:
                    output.append([nums[i], nums[j], nums[k]])
                j += 1
        return output
