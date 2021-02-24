# Given a sorted array of integers and a target value, determine if there exists two integers in the array that sum
# up to the target value.
# See if you can solve this in O(N) time and O(1) auxiliary space.


def sorted_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            print(f"{arr[left]} plus {arr[right]} is equal to {target}")
            return True

        if arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1

    return False


if __name__ == "__main__":
    print(sorted_sum([2, 3, 4, 5, 8, 9], 9))
