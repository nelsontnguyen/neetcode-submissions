class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for this to be an anagram, we need to track the total amount of each letters (so a map)

        # obviously, if the length of the strings are differnt they are not anagrams

        if len(s) != len(t):
            return False
        
        # define dictionaries
        cS, cT = {}, {}

        # for index from 0 to len of s - 1
        for i in range(len(s)):
            cS[s[i]] = 1 + cS.get(s[i], 0)
            cT[t[i]] = 1 + cT.get(t[i], 0)
        
        return cS == cT