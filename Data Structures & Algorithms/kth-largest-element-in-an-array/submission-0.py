class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # find max heap and drop of the array
        # until k = 0
        nums.sort(reverse=True)
        nums = nums[0 + k - 1:]
        return nums[0]