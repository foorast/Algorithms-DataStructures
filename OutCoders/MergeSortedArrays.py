# Given two sorted arrays of integers, combine the values into one sorted array?
# Input: [1,3,5], [2,4,6,8,10]
# Output: [1,2,3,4,5,6,8,10]
# See if you can solve this in O(N+M) time and O(N+M) auxiliary space.


def merge_arrays(arr1, arr2):
    merged = []
    arr1_tracker = 0
    arr2_tracker = 0

    while len(merged) < (len(arr1) + len(arr2)):
        if arr1_tracker > len(arr1) - 1:
            merged.extend(arr2[arr2_tracker:])
            break

        if arr2_tracker > len(arr2) - 1:
            merged.extend(arr1[arr1_tracker:])
            break

        if arr1[arr1_tracker] < arr2[arr2_tracker]:
            merged.append(arr1[arr1_tracker])
            arr1_tracker += 1
        else:
            merged.append(arr2[arr2_tracker])
            arr2_tracker += 1

    return merged


if __name__ == "__main__":
    x = [1, 3, 5]
    y = [2, 4, 6, 8, 10]

    print(merge_arrays(x, y))
