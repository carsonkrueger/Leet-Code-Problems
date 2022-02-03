from typing import DefaultDict


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        counter = 0
        saved = DefaultDict(lambda: 0)

        for i in nums1:
            for j in nums2:
                saved[i+j] += 1

        
        for i in nums3:
            for j in nums4:
                if -(i+j) in saved:
                    counter += saved.get(-(i+j))
        
        return counter
        
if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]

    sol = Solution()
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))