import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse=True)
        # nums = nums[0 + k - 1:]
        # return nums[0]
        k = len(nums) - k


        def quickSelect(l,r):
            pivotIndex =  random.randint(l,r)
            nums[pivotIndex], nums[r] = nums[r], nums[pivotIndex]
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k: return quickSelect(l, p -1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]
        return quickSelect(0, len(nums) - 1)
        # selecting default last element as pivot will run into
        # max recursion depth issue where the array is sorted
        # solution: select by random and move to the end of array 