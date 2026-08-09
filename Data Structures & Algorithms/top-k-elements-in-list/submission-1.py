class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap for occurence
        count = {}

        # array of arrays, in the inner array we'll be adding numbers with that count (so like at index 2 we'll have an array of numbers that count to 2). Also, len(nums) + 1 because of 0-index basing
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # put a default of 0 in-case it doesn't exist in current map (why we use hashmap)
        for n, c in count.items(): # returns the key and value as pairs
            freq[c].append(n) # count is the index; the number n occurs c amount of times (we're appending to the empty arrays)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: # freq[i] is a sub list
                res.append(n)
                if len(res) == k:
                    return res





        