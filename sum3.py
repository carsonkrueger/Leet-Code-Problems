class Solution:
    def threeSum(self, nums: list[int] ):
        # nums.sort()
        res = []
        neg = []
        zer = []
        pos = []
        for i in nums:
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)
            else:
                zer.append(i)
        # for i in range(len(nums)):

if __name__ == "__main__":
    sol = Solution()
    sol.threeSum([-1,-2,2,4,0,0,1])