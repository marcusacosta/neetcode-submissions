class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        sorted_nums = sorted(freq,key=freq.get,reverse=True)
        res = sorted_nums[:k]

        return res

            
        
        