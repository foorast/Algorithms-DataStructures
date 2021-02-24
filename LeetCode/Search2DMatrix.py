# Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the
# following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # for i in matrix:
        #     if target in i:
        #         return True
        # return False
        return any(target in row for row in matrix)


if __name__ == "__main__":
    obj = Solution()
    matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ]
    print(obj.searchMatrix(matrix, 31))
