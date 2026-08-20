class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solved = {}
        num_len = len(nums)
        res = []
        for i in range(num_len):
            diff = target - nums[i] 
            if diff in solved:
                return[solved[diff],i]
            solved[nums[i]] = i