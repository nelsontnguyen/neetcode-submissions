class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(n) timespace - Leaning towards hashmap
        hm = {}

        # We use a hashmap to store the number and it's index
        for i, n in enumerate(nums):
            hm[n] = i
        
        for i, n in enumerate(nums):
            temp = target - n
            # the logic I was close to: If the difference is found in the hashmap and the index is not the same 
            # as the current one, we return the current index with the index of the difference that is found
            if temp in hm and hm[temp] != i:
                return [i, hm[temp]]
        
