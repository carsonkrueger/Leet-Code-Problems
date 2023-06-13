class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        combos = []
        phone = {"2": ["a","b","c"], "3": ["d","e","f"], "4": ["g","h","i"], "5": ["j","k","l"], "6": ["m","n","o"], "7": ["p","q","r","s"], "8": ["t","u","v"], "9": ["w","x","y","z"]}

        def create_next_combo(combo: str, next_digits):
            if not next_digits:
                combos.append(combo)
            else:
                for letter in phone[next_digits[0]]:
                    create_next_combo(combo + letter, next_digits[1:])

        create_next_combo("", digits)

        return combos

if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))
    digits = ""
    print(sol.letterCombinations(digits))
    digits = "476"
    print(sol.letterCombinations(digits))