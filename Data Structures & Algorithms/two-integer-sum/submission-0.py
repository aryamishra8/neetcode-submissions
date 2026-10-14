class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        my logic
        for loop which sums and check?
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


        