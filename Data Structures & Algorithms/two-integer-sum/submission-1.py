class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        my logic
        for loop which sums and check?
        """
        for i in range(len(nums)): #to get position of values in array
            for j in range(len(nums)): #same
                if nums[i] + nums[j] == target and i != j: #core checking
                    return [i, j] #return the ones that matched dont add else


        