class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        if n==0:
            return result
        leftProduct , rightProduct = [0]*n , [0]*n

        product=1
        for i in range(0,n):
            product*=nums[i]
            leftProduct[i]=product

        product=1
        for i in range(n-1,-1,-1):
            product*=nums[i]
            rightProduct[i]=product

        result[0]=rightProduct[1]
        result[n-1]=leftProduct[n-2]

        for i in range(1,n-1):
            result[i]=leftProduct[i-1]*rightProduct[i+1]
        return result      