class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # tale as old as time, we'll use a hashmap

        # we are instantiating a temp dictionary (it's empty at the moment)
        temp = {}

        # for (index, numberical value) in nums
        for i, n in enumerate(nums):
            # difference between target and current number
            diff = target - n

            # if it exists, we return it otherwise we add to the temp dictionary
            if diff in temp:
                return [temp[diff], i]
            temp[n] = i
        

