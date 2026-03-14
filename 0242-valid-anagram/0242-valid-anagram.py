class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_array=sorted(s)
        t_array=sorted(t)

        i=0
        while i<len(s_array):
            if s_array[i]!=t_array[i]:
                return False
            i+=1
        return True
        