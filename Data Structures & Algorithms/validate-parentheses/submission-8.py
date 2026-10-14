class Solution:
    def isValid(self, s: str) -> bool:

        parens = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []

        for str in s:
            if str in parens.values():
                stack.append(str)
            elif str in parens.keys():
                if len(stack) == 0:
                    return False
                if parens[str] != stack.pop():
                    return False

        return len(stack) == 0
        