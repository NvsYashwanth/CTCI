# Approach - 1
class Solution:
    def URLify(self,string,true_length):
        string = string.strip() 
        space_count = string.count(' ') 
        new_length = true_length + space_count * 2

    
        # Start filling character from end 
        index = new_length - 1
    
        string = list(string) 
    
        # Fill string array 
        for f in range(true_length - 2, new_length - 2): 
            string.append('0') 
    
        # Fill rest of the string from end 
        for j in range(true_length - 1, 0, -1): 
    
            # inserts %20 in place of space 
            if string[j] == ' ': 
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index = index - 3
            else: 
                string[index] = string[j] 
                index -= 1
    
        return ''.join(string) 

sol=Solution()
print(sol.URLify('MR John Smith  ',13))
print(sol.URLify('much ado about nothing      ', 22))
