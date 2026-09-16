from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        ans=0
        prefix_count = defaultdict(int)
        prefix_count[0]+=1
        for i in range(len(nums)):
            presum += nums[i]
            ans+= prefix_count[presum - k]
            prefix_count[presum]+=1
        return ans