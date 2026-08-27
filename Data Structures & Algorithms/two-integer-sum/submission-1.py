class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,x in enumerate(nums):
            complement=target-x
            if complement in map:
                return [map[complement],i]
            map[x]=i