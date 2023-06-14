class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if (bracket == "(" or bracket == "[" or bracket == "{"):
                stack.append(bracket)
                continue
            
            if (len(stack) == 0):
                return False
            
            if (bracket == ")"):
                if stack.pop() != "(":
                    return False
            elif (bracket == "]"):
                if stack.pop() != "[":
                    return False
            elif (bracket == "}"):
                if stack.pop() != "{":
                    return False
                
        if (len(stack) != 0): 
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    s = "()"
    print(sol.isValid(s))
    s = "()[]{}"
    print(sol.isValid(s))
    s = "(]"
    print(sol.isValid(s))