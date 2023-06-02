from collections import Counter

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        cnt=0
        c=Counter(nums)
        
        if k==0:
            for key,v in c.items():
                if v>1:
                    cnt+=1
        else:
            for key,v in c.items():
                if key+k in c:
                    cnt+=1
        return cnt
            


            

        
def main():
    # print("LEN", len(s))
    sol = Solution()
    print(sol.findPairs([1,2,3,4,5], 1))


if __name__ == "__main__":
    main()