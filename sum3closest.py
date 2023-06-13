class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        numsLen = len(nums)

        bestSumation = None

        for i in range(numsLen-2):
            iNum = nums[i]
            left = i + 1
            right = numsLen - 1

            while (left < right):
                leftNum = nums[left]
                rightNum = nums[right]

                sumation = iNum + leftNum + rightNum
                if (bestSumation == None):
                    bestSumation = sumation
                elif (abs(sumation - target) < abs(bestSumation - target)):
                    bestSumation = sumation

                if (sumation < target):
                    left += 1
                elif (sumation > target):
                    right -= 1
                else:
                    return sumation
                
        return bestSumation

if __name__ == "__main__":
    sol = Solution()
    nums = [-2,0,0,2,2]
    print(sol.threeSumClosest(nums, 1))
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSumClosest(nums, 1))
    nums = [-1,2,1,-4]
    print(sol.threeSumClosest(nums, 1))