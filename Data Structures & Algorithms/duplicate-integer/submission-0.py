class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # numbers we have already seen
        for n in nums: #check each number
            if n in seen: #seen it before?
                return True # duplicate found
            seen.add(n) #remember it
        return False
        