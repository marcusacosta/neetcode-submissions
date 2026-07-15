class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if strings arent the same length return false
        if len(s) != len(t):
            return False
        #build both the hashmaps
        countS, countT = {}, {}
        #iterate through the str, then populate them
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        #iterate through one of the hashmaps, then compare chars
        return countS == countT