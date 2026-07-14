class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set to track the nums visited
        numSet = set(nums)
        # track the longest sequence
        longest = 0

        for n in nums:
            # check if it's the first in sequence
            if (n - 1) not in numSet:
                length = 0

                while (n + length) in numSet:
                    length += 1
                    longest = max(length, longest)

        return longest