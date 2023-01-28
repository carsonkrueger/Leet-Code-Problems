class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {"M":1000, "CM":900, "D":500, "CD":400, "6":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        res: str= ""
        for i in range(len(symbols)):
            if (symbols[i] <= num):
                res += symbols[i]
                i -= 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(1994))