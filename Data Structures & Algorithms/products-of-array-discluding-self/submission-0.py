class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = [nums[0]] * n
        suf_product = [nums[-1]] * n
        for i in range(1,n):
            pre_product[i]=nums[i]*pre_product[i-1]
            suf_product[n-i-1]=nums[n-i-1]*suf_product[n-i]
        ans =[0]*n
        for i in range(1,n-1):
            ans[i] = pre_product[i-1]*suf_product[i+1]
        ans[0]=suf_product[1]
        ans[n-1]=pre_product[n-2]
        return ans
            
