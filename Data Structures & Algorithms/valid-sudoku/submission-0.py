class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # I have no idea where to start

        # Solution
        #   - We will first detect duplicates using a hashset for both rows and cols
        #   - We want to iterate over entire grid
        #   - We know the dimensions of the board, which is 9 x 9
        #   - Empty pos referred as ".", so we first check if empty
        #   - next thing we want to check is "Have we found the duplicate?"
        #       - If we have, we return false immediately

        cols = collections.defaultdict(set) # hashmap: key is col num
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue # we skip the empty
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]): # the logic here is that the current row/col we are in is a duplicate (since rows is a hashset)
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True





