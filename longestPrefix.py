class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        totalStr = ""
        while True:
            try:
                curLetter = strs[0][i]
                for s in strs:
                    if curLetter != s[i]:
                        return totalStr
                i += 1
                totalStr += curLetter

            except IndexError:
                return totalStr

if __name__ == "__main__":
    strs = ["f","flow","flight"]
    sol = Solution
    print(sol.longestCommonPrefix(sol, strs=strs))