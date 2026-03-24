class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right, maxArea = 0, len(height) - 1, 0
        while left<right:
            currentHeight = min(height[left], height[right])
            breadth = right - left
            area = currentHeight * breadth
            maxArea = max(maxArea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
