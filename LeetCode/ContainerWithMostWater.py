# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
# lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which,
# together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0

        while start < end:
            area = max(area, (min(height[start], height[end]) * (end - start)))

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return area


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxArea([1, 1]))
    print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(obj.maxArea([4, 3, 2, 1, 4]))
    print(obj.maxArea([1, 2, 1]))
