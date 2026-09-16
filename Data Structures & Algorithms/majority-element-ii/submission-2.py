from math import ceil
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <3:
            return list(set(nums))
        ans = []
        limit = n//3
        nums.sort()
        count = 0
        for i in range(1,n):
            if nums[i]== nums[i-1]:
                count+=1
            else:
                count+=1
                if count > limit:
                    ans.append(nums[i-1])
                count = 0
        if nums[-2] == nums[-1]:
            count+=1
            if count > limit:
                ans.append(nums[-1])
        return ans
                