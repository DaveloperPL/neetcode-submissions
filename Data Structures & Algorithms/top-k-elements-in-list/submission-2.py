class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}

        for x in nums:
            arr[x] = arr.get(x, 0) + 1

        returnArr = []

        for _ in range(k):
            z = max(arr, key=arr.get)
            returnArr.append(z)
            arr[z] = 0

        return returnArr
