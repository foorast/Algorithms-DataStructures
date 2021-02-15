# Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of
# the k weakest rows in the matrix ordered from the weakest to the strongest.
#
# A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j,
# or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row,
# that is, always ones may appear first and then zeros.


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        my_dict = {}
        tracker = 0
        count = 0
        for i in mat:
            for j in i:
                if j == 1:
                    count += 1
            my_dict[tracker] = count
            tracker += 1
            count = 0
        sorted_tuple = sorted(my_dict.items(), key=lambda item: item[1])
        sorted_dict = {k: v for k, v in sorted_tuple}
        my_list = list(sorted_dict.keys())
        return my_list[0:k]


if __name__ == "__main__":
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]

    obj = Solution()
    print(obj.kWeakestRows(mat, 3))
