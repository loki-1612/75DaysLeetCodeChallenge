class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        n=len(nums)
        k=0
        for i in range(n):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        
        for num in range(k,n):
            nums[k]=0
            k+=1
                
            

            



        
                
       
        