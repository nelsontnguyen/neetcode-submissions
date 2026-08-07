class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # First check correction: easy constraint to get rid of is that if they're not equal in length,
        # there is no way that they are possibly anagrams

        if len(s) != len(t):
            return False

        t1_dict = {}
        t2_dict = {}

        for c in s:
            t1_dict[c] = t1_dict.get(c, 0) + 1
        
        for c in t:
            t2_dict[c] = t2_dict.get(c, 0) + 1
        
        return t1_dict == t2_dict

        