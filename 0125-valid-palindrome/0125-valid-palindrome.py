class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for i in s:
            if i.isalnum():
                res.append(i.lower())
        temp=''.join(res)
        left,right=0,len(temp)-1
        while left<=right:
            if temp[left]!=temp[right]:
                return False
            left+=1
            right-=1
        return True


        