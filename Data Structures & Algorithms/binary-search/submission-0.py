class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            item = nums[m]
            if item == target: 
                return m
            elif item < target: 
                l = m + 1
            else: 
                r = m - 1
        return -1