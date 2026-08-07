class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        l, r = 0, R * C - 1

        while l <= r:
            mid = l + (r - l) // 2
            # Basic structure of a binary search:
            # 1. Find the middle value
            # 2. If the value is less, shift r and vice versa
            row, col = mid // C, mid % C
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False
