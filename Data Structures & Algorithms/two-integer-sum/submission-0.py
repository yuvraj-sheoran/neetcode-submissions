class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            x = nums[i]
            partner = target - x
            if partner in seen:
                return [seen[partner],i]
            seen[x] = i