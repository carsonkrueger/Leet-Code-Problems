class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        i = 0
        j = len(height)-1
        for k in range(len(height)):
            wallOne = height[i]
            wallTwo = height[j]
            area = 0
            if (wallOne < wallTwo):
                area = wallOne * (j-i)
                i += 1
            else:
                area = wallTwo * (j-i)
                j -= 1
            if (area > max):
                max = area
        return max