class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Count occurrences of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Map frequencies to bucket lists
        for num, c in count.items():
            freq[c].append(num)

        res = []
        # Traverse buckets from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res