

class Solution:
    """
    Approach - 1 : Dictionary O(N) 
    without need to loop again to check for 1
    """
    def palindperm(self,s):
        s=s.lower()
        s_hash={}
        odd=0

        for i in s:
            if i.isalnum():
                if s_hash.get(i)==None:
                    s_hash[i]=1
                    odd+=1
                else:
                    s_hash[i]+=1
                    if s_hash[i]%2==0:
                        odd-=1
                    else:
                        odd+=1
        return odd<=1
    
sol=Solution()
print(sol.palindperm("Tact Coa"))
