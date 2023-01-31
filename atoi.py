
class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        pos = 0
        foundInt = False
        foundSign = False

        for i in range(len(s)):
            val = s[i]
            if val == " ":
                continue
            elif val.isnumeric():
                foundInt = True
                pos = i
                break
            elif val == "+" or val == "-":
                if foundSign:
                    return 0
                foundSign = True
                res += val
            else:
                return 0

        if foundInt:
            for i in range(pos, len(s)):
                val = s[i]
                if not val.isnumeric():
                    break
                res += s[i]
            num = int(res)
            if num > 2147483647:
                return 2147483647
            elif num < -2147483648:
                return -2147483648
            return num
        return 0

def main():
    s = "   -2147483748 hello"
    # print("LEN", len(s))
    sol = Solution()
    print(sol.myAtoi(s))


if __name__ == "__main__":
    main()
