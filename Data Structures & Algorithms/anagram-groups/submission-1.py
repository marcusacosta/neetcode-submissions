class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use defaultdict(list) because we need to return a list of arrays in the res eg [[cat, act]]
        res = defaultdict(list)
        
        #loop through strs arr to build the char freq list
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            res[key].append(s)

        return list(res.values())

