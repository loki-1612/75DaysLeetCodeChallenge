class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(n-1):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                low=i+1
                high=n-1
                target=-nums[i]
                while low<high:
                    current_sum=nums[low]+nums[high]
                    if current_sum==target:
                        result.append([nums[i],nums[low],nums[high]])
                        while low<high and nums[low]==nums[low+1]:
                            low+=1
                        while low<high and nums[high]==nums[high-1]:
                            high-=1
                        low+=1
                        high-=1
                    elif current_sum>target:
                        high-=1
                    else:
                        low+=1
        return result
        