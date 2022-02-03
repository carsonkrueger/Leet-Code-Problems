class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        saved = {}

        for index in range(nums_len):
            difference = target - nums[index]

            if difference in saved:
                return [saved.get(difference), index]
            
            saved[nums[index]] = index
               
if __name__ == "__main__":
    nums = [3,3]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
