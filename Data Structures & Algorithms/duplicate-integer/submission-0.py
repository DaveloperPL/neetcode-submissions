class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for x in nums:
            map[x] = 0
        for x in nums:
            map[x]+=1
            if (map[x] > 1):
                return True

        return False