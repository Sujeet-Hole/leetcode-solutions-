
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashmap = {}

        for index, num in enumerate(nums):
            if num in hashmap:
                if abs(hashmap[num] - index) <= k:
                    return True

            hashmap[num] = index

        return False
