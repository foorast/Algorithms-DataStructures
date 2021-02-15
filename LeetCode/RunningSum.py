class Solution(object):
    def runningSum(self, nums):
        temp_list = []
        count = 0
        for i in nums:
            count += i
            temp_list.append(count)
        return temp_list


if __name__ == "__main__":
    tp = [1, 2, 3, 4]
    obj = Solution()
    print(obj.runningSum([1, 2, 3, 4]))
