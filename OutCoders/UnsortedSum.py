# Given an array of integers, and a target value determine if there are two integers that add to the sum.
# Input: [4,2,6,5,7,9,10], 13
# Output: true


def unsorted_sum(arr, target):
    my_dict = {}
    for i in arr:
        if target - i in my_dict:
            return True
        my_dict[i] = i

    return False


if __name__ == "__main__":
    print(unsorted_sum([4, 2, 6, 5, 7, 9, 10], 13))
