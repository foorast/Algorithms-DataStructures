# Given a bit array, return it sorted in-place (a bit array is simply an array that contains only bits, either a 1 or
# a 0).
# See if you can solve this in O(N) time and O(1) auxiliary space.


def sort_bit_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:

        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]

        if arr[left] == 0:
            left += 1

        if arr[right] == 1:
            right -= 1


if __name__ == "__main__":
    arr1 = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0]
    sort_bit_array(arr1)
    print(arr1)
