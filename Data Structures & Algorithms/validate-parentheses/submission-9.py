class Solution:
    def isValid(self, s: str) -> bool:

        parens = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []

        for char in s:
            if char in parens.values():
                stack.append(char)
            elif char in parens.keys():
                if len(stack) == 0:
                    return False
                if parens[char] != stack.pop():
                    return False

        return len(stack) == 0
        