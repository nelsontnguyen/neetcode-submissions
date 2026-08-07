class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need to output a result output array (no extra memory)

        res = [1] * len(nums) # we give each position a value of one

        pfix = 1
        for i in range(len(nums)):
            res[i] = pfix
            pfix *= nums[i] # how we compute prefix as we iterate

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #How we iterate backwards
            res[i] *= postfix
            postfix *= nums[i]
        return res

