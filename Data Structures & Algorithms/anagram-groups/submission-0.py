class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we are going to use a hashtable

        # Defaultdict basically allows you to initialize unseen keys 
        # using a function, so we could rewrite the above as:
        res = defaultdict(list)

        for s in strs:
            # each letter is from lowercase a to lowercase z, meaning we can instantiate:
            count = [0] * 26 # there are 26 letters in the alphabet, and a - z using ascii logic can give us
            # indices in range from 0-26

            for c in s:
                count[ord(c) - ord('a')] += 1 # increases count of current letter in the current string
            res[tuple(count)].append(s) # appends the current string as a value to the curr hashtable
        return list(res.values()) #retrieves the values 

        # lists cannot be keys, so tuples are non-mutable