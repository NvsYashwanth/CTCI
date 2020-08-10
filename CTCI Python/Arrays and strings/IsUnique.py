
# Approach - 1 - Very Fast
class Solution():
    def uniqueChars(self,string):
        # Assuming character set is ASCII (128 characters)
        # Note : Extended ASCII has 256 characters

        chars = [False for i in range(128)]
        for char in string:
            val = ord(char)
            if chars[val]:
                # Char already found in string
                return False
            chars[val] = True

        return True

sol=Solution()
print(sol.uniqueChars('abeirjwpj'))

#--------------------------------------------------

# Approach - 2 
class alternateSolution:
    def uniqueChars(self,s):
        d={}
        for i in s:
            if d.get(i)==None:
                d[i]=1
            else:
                d[i]+=1
        if len(d)!=len(s):
            return False
        return True

solalt = alternateSolution()
print(solalt.uniqueChars('abeirjwpj'))

#--------------------------------------------------


# Approach - 3 Without additional data structure wiht iterations
'''
This will take O(n**2) as we need to check
through for loops and iterate over every letter
'''
#--------------------------------------------------


# Approach - 4 Without additional data structure with sorting
'''
This will take O(nlogn)
'''



