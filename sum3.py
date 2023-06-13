class Solution:
    def threeSum(self, nums: list[int] ):
        nums.sort()
        solutionList: list[list[int]] = []
        numsLen = len(nums)

        for i in range(numsLen-2):
            iNum = nums[i]
            left = i + 1
            right = numsLen - 1

            while (left < right):
                leftNum = nums[left]
                rightNum = nums[right]

                sum = leftNum + rightNum + iNum

                if (sum < 0):
                    left += 1
                elif (sum > 0):
                    right -= 1
                else:
                    if (i != 0 and nums[i]==nums[i-1]):
                        left += 1
                        right -= 1
                        continue
                    elif ((left!=i+1 and right != numsLen-1) and (nums[left]==nums[left-1] and nums[right]==nums[right+1])):
                        left += 1
                        right -= 1
                        continue
                    solutionList.append([iNum, leftNum, rightNum])
                    left += 1
                    right -= 1

        return solutionList


if __name__ == "__main__":
    sol = Solution()
    nums = [-2,0,0,2,2]
    print(sol.threeSum(nums))
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(sol.threeSum(nums))