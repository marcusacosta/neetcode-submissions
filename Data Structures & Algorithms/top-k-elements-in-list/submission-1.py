class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [ [] for _ in range(len(nums) + 1)]
        #populate the count
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        #populate the freq
        for num,cnt in count.items():
            freq[cnt].append(num)
        #collect top 'K' elements
        res = []
        for i in range(len(freq) - 1,0,-1):
          if freq[i]:
            for num in freq[i]:
                res.append(num) 
                if len(res) == k:
                    return res