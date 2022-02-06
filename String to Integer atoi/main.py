from math import trunc

class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        s = s.strip(" ")

        index = 0
        signed = 1
        new_s = ""

        if s[0] == "-":
            signed = -1
            index += 1
        elif s[0] == "+":
            index += 1
        if s[index] == "-" or s[index] == "+":
                return 0

        while(index < len(s)):
            if s[index] == "-" or s[index] == "+":
                return 0

            if s[index].isnumeric():
                if s[index] == "0":
                    continue
                new_s += s[index]
                index += 1

            elif not s[index].isnumeric() and new_s == "":
                return 0

            else:   # non numeric
                break

        new_s = int(new_s)

        if new_s > (2 ** 31):
            new_s = 2 ** 31

        return new_s * signed
        # for i in range(len(s)):
        #     if s[left_pointer] == "0" or s[left_pointer] == "+":  # Skips leading zeros and moves left pointer up 1         
        #         left_pointer += 1

        #     elif s[left_pointer] == "-":  # Records '-' sign
        #         signed = -1
        #         left_pointer += 1

        #     elif not s[left_pointer].isnumeric(): # Return 0 if non numeric chars are detected
        #         return 0

        #     if not s[right_pointer].isnumeric(): # Moves right pointer down 1
        #         if s[right_pointer] == "-":         # Records '-' sign
        #             signed = -1         
        #         right_pointer -= 1

        #     elif s[left_pointer].isnumeric() and s[left_pointer] != "0" and s[right_pointer].isnumeric(): # Found the number in the string
        #         s = int(float(s[left_pointer:right_pointer+1]))
        #         break

        #     if left_pointer == right_pointer:
        #         return 0
        
        
        


def main():
    s = "   -42"
    # print("LEN", len(s))
    sol = Solution()
    print(sol.myAtoi(s))


if __name__ == "__main__":
    main()
