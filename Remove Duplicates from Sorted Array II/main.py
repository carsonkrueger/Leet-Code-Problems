class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # saved = {}
        # i = 0

        # while(i < len(nums)):
        # # loop thru nums
        #     if int(saved.get(nums[i])) >= 2:
        #     # if nums[i] has more than 2 occurences in saved
        #         nums.remove(nums[i])
        #         # remove nums[i]
        #     else:
        #     # else does not hav
        #         if nums[i] in saved:
        #             saved[i] += 1
        #         # increment saved[i] key by one
        #         else:
        #             saved[i] = 1
        #         i += 1
        
        # print(nums)
        # return len(nums)

        i = 0
        curr_cnt = 0
        prev_num = None
        
        while(i < len(nums)): # while i < len(nums):
            if prev_num == nums[i]: # if prev_num is same as nums[i]
                if curr_cnt >= 2: # if curr_cnt is 2 or more
                    nums.remove(nums[i]) # remove nums[i]
                    continue
                
                else: # else curr_cnt is 1
                    curr_cnt += 1 # increment curr_cnt
                    

            else: # else prev_num is not same as nums[i]:
                curr_cnt = 1
                prev_num = nums[i]
                # reset vars
            i += 1
        
        print(nums)
        return(len(nums))


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    saved = {}
    saved[1] = 2
    sol = Solution()
    sol.removeDuplicates(nums)
