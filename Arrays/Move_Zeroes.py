class Solution:
   # 1st solution
    '''    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for num in nums:
            if num != 0:
                nums[non_zero_index] = num
                non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0'''

    # 2nd solution
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [num for num in nums if num != 0] + [0] * (len(nums) - len([num for num in nums if num != 0]))
 