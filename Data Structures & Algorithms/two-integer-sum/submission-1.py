class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for idx, value in enumerate(nums):
            diff = target - value
            if diff in res:
                return [res[diff], idx]
            res[value] = idx