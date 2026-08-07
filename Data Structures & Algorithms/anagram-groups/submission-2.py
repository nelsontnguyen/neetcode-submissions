class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # default dictionary where the default value is a list

        for s in strs:
            count = [0] * 26
            for c in s:
                # ascii value
                count[ord(c) - ord('a')] += 1 # count is a list, and a list cannot be a key
            # we put into tuple because of this
            res[tuple(count)].append(s)
        return list(res.values())
        