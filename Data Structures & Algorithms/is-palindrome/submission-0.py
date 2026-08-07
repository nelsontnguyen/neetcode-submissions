class Solution:
    def isPalindrome(self, s: str) -> bool:
        # in this problem, we can only accept letters from A-Z, a-z, and 0-9
        #   - This condition can be found using the ord function
        #       - ord function: a built-in function that takes a single Unicode character as input and returns its corresponding Unicode code point as an integer
        # this is the solution, take notes and try to understand

        l, r = 0, len(s) - 1
        
        while l < r:
            # the two while liips will determine if the current char is within the range, if not we update pointer location
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): # The actual test
                return False
            l, r = l + 1, r - 1
        return True
    
    # This helper function determines if the current char is within this threshold (useful to know)
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9')) 