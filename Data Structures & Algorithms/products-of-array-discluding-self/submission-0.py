class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        for index in range(len(nums)):
            for entry in range(len(nums)):
                if entry != index: 
                    product *= nums[entry]
            res.append(product)
            product = 1
        return res