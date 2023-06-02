class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        res: str= ""
<<<<<<< HEAD
        while (num != 0):
            for ch in symbols:
                val = symbols[ch]
                while val <= num:
                    num -= val
                    res += ch
=======
        for key, val in symbols.items():
            multiple = num // val
            if multiple > 0:
                res += (multiple * key)
                num -= (multiple * val)
>>>>>>> c7bd529d081cd4631574f31d1492ad20c0abe050
        return res

if __name__ == "__main__":
    sol = Solution()
<<<<<<< HEAD
    print(sol.intToRoman(20))
=======
    print(sol.intToRoman(100))
>>>>>>> c7bd529d081cd4631574f31d1492ad20c0abe050
