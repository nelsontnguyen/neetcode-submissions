class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        t1_dict = {}
        t2_dict = {}

        for c in s:
            t1_dict[c] = t1_dict.get(c, 0) + 1
        
        for c in t:
            t2_dict[c] = t2_dict.get(c, 0) + 1
        
        return t1_dict == t2_dict

        