class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()

        for i in range(len(nums) - 1):
            curr = nums[i] + nums[i + 1]

            if curr in s:
                return True

            s.add(curr)

        return False