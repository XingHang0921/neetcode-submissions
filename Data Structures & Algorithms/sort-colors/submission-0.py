class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
        for color in nums:
            count[color] += 1
        i = 0
        for color in range(0, 3):
            while count[color] > 0:
                nums[i] = color
                i += 1
                count[color] -= 1