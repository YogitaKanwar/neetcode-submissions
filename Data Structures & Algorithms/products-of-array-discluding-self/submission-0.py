class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # PASS 1: left to right — bake in prefix products
        running_prefix = 1
        for i in range(n):
            answer[i] = running_prefix
            running_prefix *= nums[i]

        # PASS 2: right to left — fold in suffix products
        running_suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= running_suffix
            running_suffix *= nums[i]

        return answer