class Solution:
    def rob(self, nums: List[int]) -> int:
        skip, take = 0, 0

        for num in nums:
            temp = max(take + num, skip)
            take = skip
            skip = temp
        return skip