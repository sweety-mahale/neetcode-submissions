class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt= {}
        for i in range(0, len(nums)):
            if((target-nums[i]) in cnt):
                return [cnt[target-nums[i]], i]
            cnt[nums[i]]=i
        return []