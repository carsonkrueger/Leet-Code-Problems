class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        combos = []

        def recFindCombo(s, left = 1, right = 0):
            if (len(s) == n*2):
                combos.append(s)
                return

            if (left < n):
                recFindCombo(s + "(", left + 1, right)
            if (right < left):
                recFindCombo(s + ")", left, right + 1)

        recFindCombo("(")
        return combos
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(1))
    print(sol.generateParenthesis(2))
    print(sol.generateParenthesis(3))