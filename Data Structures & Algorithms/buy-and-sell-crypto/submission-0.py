class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this might point to a brute-force or a two-pointer solution

        # we were right on two pointer but we could also use a d-p
        # instantiate a left and right pointer (we are going to update the right pointer)
        l, r = 0, 1

        max_p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                # we update the left pointer to move up
                l = r
            # to exit the loop and not repeat forever
            r += 1
        return max_p