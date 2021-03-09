"""
Given an array of positive integers and a target value, return true if there is a subarray of
consecutive elements that sum up to this target value.

Input: Array of integers, target value
Output: Boolean

Input: [6,12,1,7,5,2,3], 14      	=>	Output: true (7+5+2)
Input: [8,3,7,9,10,1,13], 50		=>	Output: false

target greater the sum all values
traget < smallest values

TIme: O(N)
Space: O(1)

index i = 0
index j = 0
                              0   1   2  3  4  5  6
                              6, 12, 1,  7, 5, 3, 3

                              j + 1

                              6, 12 = 18 > target 14

                              i + 1

                              12, 1 < target

                              j + 1

                              12, 1, 7 > target

                              i + 1

                              1, 7 < target

                              j + 1

                              1, 7, 5, 2 > target

                              i + 1
                              j i + 1

                              7, 5 < taget

                              j + 1

                              7, 5, 2 = target
                                return true


    index i eqauls 0
    index j equals 1

    if sum of all elements in array of integers less than target
      return false

    if target less than minimum element in array of integers
      return false

    if target is in array of integers
      return true

    while i less than length of array of integers
      if j greater than array of integers:
        i += 1
        j = i + 1
        continue

      if array[i] plus array[j] greater than target
        i += 1
        j = i + 1
        continue

      if the sum of splice array[i:j+1]
        Return True

      j += 1


    return false

"""


def consecutive_sum(arr, target):
    i = 0
    j = 0

    if sum(arr) < target:
        return False

    if target < min(arr):
        return False

    if target in arr:
        return True

    while i < len(arr) - 1:
        if j > len(arr) - 1:
            i += 1
            j = i + 1
            continue

        if sum(arr[i:j + 1]) > target:
            i += 1
            j = i + 1
            continue
        elif sum(arr[i:j + 1]) == target:
            return True
        else:
            j += 1

    return False


if __name__ == "__main__":
    print(consecutive_sum([6, 12, 1, 7, 5, 2, 3], 14))
