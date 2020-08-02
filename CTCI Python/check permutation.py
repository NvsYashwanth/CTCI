# Approach - 1 : Sorting and checking equality - O(nlogn) time
class Solution:
    def checkperm(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        return sorted(s1)==sorted(s2)

sol=Solution()
print(sol.checkperm('god','dog'))

#---------------------------------------------------------

# Approach - 2 : Using dictionary and checking character counts - O(N) time
class altsolution:
    def checkperm(self,s1,s2):
        x={}
        y={}
        if len(s1)!=len(s2):
            return False
        for i,j in zip(s1,s2):
            if x.get(i)==None:
                x[i]=1
            else:
                x[i]+=1

            if y.get(j)==None:
                y[j]=1
            else:
                y[j]+=1
        return x==y

altsol=altsolution()
print(altsol.checkperm('abgh','hgab'))
