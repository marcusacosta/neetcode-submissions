class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        '''4#neet4#code4#love3#you'''
        res,i = [],0
        while i < len(s):
            pound_pos = s.find('#',i)
            length = int(s[i:pound_pos]) #ie: 4
            res.append(s[pound_pos + 1: pound_pos + 1 + length])
            i = pound_pos + 1 + length
        return res
