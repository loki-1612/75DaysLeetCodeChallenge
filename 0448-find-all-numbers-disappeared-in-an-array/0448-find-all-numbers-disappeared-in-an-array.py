class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            value=abs(nums[i])
            index = value - 1
            if (nums[index]>0):
                nums[index]=-nums[index]
        res=[]
        for i in range(len(nums)):
            if(nums[i]>0):
                res.append(i+1)
        return res

      
        
       
        
        
        


        
    


        