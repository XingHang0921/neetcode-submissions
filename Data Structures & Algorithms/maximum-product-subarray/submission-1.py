class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = 1
        curMin = 1
        curProduct = 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            temp = curMax * n
            curMax = max(temp, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(curMax, res)
        return res
            
