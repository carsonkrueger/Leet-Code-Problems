class Solution:
    def threeSum(self, nums: list[int] ):
        nums.sort()
        solutionList: list[list[int]] = []
        numsLen = len(nums)

        for i in range(numsLen):
            iNum = nums[i]
            left = 0
            right = numsLen - 1
            for _ in range(numsLen):
                if (i>0 and nums[i-1]==nums[i]):
                    continue
                elif (left == right):
                    break
                
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue

                total = nums[left] + nums[right] + iNum

                if (total < 0):
                    left += 1
                elif (total > 0):
                    right -= 1
                elif (total == 0):
                    sol = [nums[left], nums[right], iNum]
                    sol.sort()
                    if (sol not in solutionList):
                        solutionList.append(sol)
                        break
                    right -= 1

        return solutionList


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(sol.threeSum(nums))