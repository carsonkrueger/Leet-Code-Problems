class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        saved = {}

        for index in range(len(nums)):
            difference = target - nums[index]

            if difference in saved:
                return [saved.get(difference), index]
            
            saved[nums[index]] = index
               
if __name__ == "__main__":
    nums = [3,-2,5,6,2,3,3,8]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
