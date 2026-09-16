from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        ans=0
        prefix_count = defaultdict(int)
        for i in range(len(nums)):
            presum += nums[i]
            ans+= prefix_count[presum - k]
            prefix_count[presum]+=1
            if presum == k:
                ans+=1
        return ans