# The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order.  The
# integer in the i^{th}i th row of the file gives you the i^{th}i th entry of an input array.
#
# Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.  As you
# know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three
# different pivoting rules.
#
# You should not count comparisons one-by-one.  Rather, when there is a recursive call on a subarray of length mm,
# you should simply add m-1m−1 to your running total of comparisons.  (This is because the pivot element is compared
# to each of the other m-1m−1 elements in the subarray in this recursive call.)
#
# WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can
# give you differing numbers of comparisons.  For this problem, you should implement the Partition subroutine exactly
# as it is described in the video lectures (otherwise you might get the wrong answer).
#
# DIRECTIONS FOR THIS PROBLEM:
#
# 1. For the first part of the programming assignment, you should always use the first element of the array as the pivot
# element.
#
# 2. Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot
# element.  Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.
#
# 3. Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.  [The primary
# motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that
# are nearly sorted or reverse sorted.]  In more detail, you should choose the pivot as follows.  Consider the first,
# middle, and final elements of the given array.  (If the array has odd length it should be clear what the "middle"
# element is; for an array with even length 2k2k, use the k^{th}k th element as the "middle" element. So for the
# array 4 5 6 7,  the "middle" element is the second one ---- 5 and not 6!)  Identify which of these three elements
# is the median (i.e., the one whose value is in between the other two), and use this as your pivot.  As discussed in
# the first and second parts of this programming assignment, be sure to implement Partition exactly as described in
# the video lectures (including exchanging the pivot element with the first element just before the main Partition
# subroutine).
#
# EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4
# is the median of the set {1,4,8}, you would use 4 as your pivot element.


def partition(arr1, low, high):
    pivot = arr1[low]
    i = low + 1
    for j in range(low + 1, high):
        if arr1[j] < pivot:
            arr1[j], arr1[i] = arr1[i], arr1[j]
            i += 1
    arr1[low], arr1[i - 1] = arr1[i - 1], arr1[low]
    return i - 1


def quickSort(arr1, low, high):
    if low >= high:
        return
    pivotPoint = partition(arr1, low, high)
    quickSort(arr1, low, pivotPoint - 1)
    quickSort(arr1, pivotPoint + 1, high)


if __name__ == '__main__':
    with open("QuickSort.txt", "r") as f:
        my_list = [int(i) for i in f]
    quickSort(my_list, 0, len(my_list)-1)
    print(my_list)
