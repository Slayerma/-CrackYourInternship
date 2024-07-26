class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

        Here, we will use the Dutch National Flag algorithm.
        """
        r, w, b = 0, 0, len(nums)-1
        while w <= b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
