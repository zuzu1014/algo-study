class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        
        for index, num in enumerate(nums):
            for i in range(index+1, len(nums)): 
                if(nums[index] + nums[i] == target):
                    return [index, i]