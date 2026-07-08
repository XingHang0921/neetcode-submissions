class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while(l <= r):
            medium = int((l + r)/2)
            if(nums[medium] == target):
                return medium
            if(nums[medium] < target): l = medium + 1
            else: r = medium - 1
        return -1