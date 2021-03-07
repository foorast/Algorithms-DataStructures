"""
Given tow sorted arrays, merge them to form a single, sorted array with all items in non-decreasing order.

Example: [1, 2, 3], [2, 5, 5]
Result: [1, 2, 2, 3, 5, 5]

Example: [1, 3, 5], [2, 4, 6, 7, 9, 10]
Result: [1, 2, 3, 4, 5, 6, 7, 9, 10]

Example: [], [1, 2, 4]
Result: [1, 2, 4]

Example: [], []
Result: []

Input: array, array
output: array

Two index variable i and j
i = index of first array
j = index of second array

left = i + 1
right = j + 1
Each increment compare which index is smaller

                                            i = 0, j = 0
                                /                                                       \
                            1, 0                                                        0,1
                /                       \                                       /                   \
            2, 0                         1, 1                                1, 1                    0, 2
    /               \           /                   \                   /           \               /           \
    3, 0            2, 1        2,1                1,2               2,1           1,2            1,2          0,3
    /   \                    /       \          /       \                                                    /      \
4,0(base)   3,1             3,1     2,2       2,2       1,3                                                1,3    0,4(B)
                \                /       \             /
                3,2            3,2       2,3          2,3
                 \                       /
                 3,3                    3,3


create empty result list
helper recursion function with variables i and j
    base case - if i is greater than the length of array a and j is less than the array b
        add the remaining elements of array b to the result list
        return out of helper function
    base case - if j is greater than the length of array a and i is less than the array b
        add the remaining elements of array a to the result list
        return out of helper function

    if value at index i of array a is less than value at index j of array b
        add the value at index i of array a to the beginning of result list
        recursive case - helper function with i + 1 and j
    else
        add the value at index j of array b to the beginning of result list
        recursive case - helper function with i, j + 1
call helper recursion function with i = 0 and j = 0
return result list
"""


def merge_arrays_recursion(a, b):
    result_list = []

    def helper(i, j):
        if len(a) == 0 or len(b) == 0:
            result_list.extend(b[j:])
            result_list.extend(a[i:])
            return
        if i > len(a) - 1 and j < len(b) - 1:
            result_list.extend(b[j:])
            return
        if j > len(b) - 1 and i < len(a) - 1:
            result_list.extend(a[i:])
            return

        if a[i] < b[j]:
            result_list.append(a[i])
            helper(i + 1, j)
        else:
            result_list.append(b[j])
            helper(i, j + 1)

    helper(0, 0)
    return result_list


def merge_arrays_looping(a, b):
    merged = []
    a_tracker = 0
    b_tracker = 0

    while len(merged) < (len(a) + len(b)):
        if a_tracker > len(a) - 1:
            merged.extend(b[b_tracker:])
            break

        if b_tracker > len(b) - 1:
            merged.extend(a[a_tracker:])
            break

        if a[a_tracker] < b[b_tracker]:
            merged.append(a[a_tracker])
            a_tracker += 1
        else:
            merged.append(b[b_tracker])
            b_tracker += 1

    return merged


if __name__ == "__main__":
    print(merge_arrays_recursion([4, 7, 9], [1, 2, 3]))
