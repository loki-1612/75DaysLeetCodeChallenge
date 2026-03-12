class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hMap={}
        
        for i in range(0,len(nums)):
            currentVal=target-nums[i]
            if currentVal in hMap:
                return hMap[currentVal],i
            else:
                hMap[nums[i]]=i
        return [-1,-1]
        