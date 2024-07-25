class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for num in nums[1:]:
            if num != nums[i]:
                i += 1
                nums[i] = num
        return i + 1
   