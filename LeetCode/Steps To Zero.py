# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even,
# you have to divide it by 2, otherwise, you have to subtract 1 from it.
class Solution:
    def num_of_steps(self, num: int, count=0) -> int:
        if num == 0:
            return count

        if num % 2 == 0:
            return Solution.num_of_steps(self, int(num / 2), count + 1)
        else:
            return Solution.num_of_steps(self, int(num - 1), count + 1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.num_of_steps(123))
