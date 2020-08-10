

class Solution:
    """
    Approach - 1 : Check if a string 
    can converted to another string with a single edit
    """
    def one_away(self,str1, str2):
        len_diff = abs(len(str1) - len(str2))
        if len_diff > 1:
            return False
        elif len_diff == 0:
            difference_count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    difference_count += 1
                    if difference_count > 1:
                        return False
            return True
        else:
            if len(str1) > len(str2):
                longer, shorter = str1, str2
            else:
                longer, shorter = str2, str1
            shift = 0
            for i in range(len(shorter)):
                if shorter[i] != longer[i + shift]:
                    if shift or (shorter[i] != longer[i + 1]):
                        return False
                    shift = 1
            return True

        
sol=Solution()
print(sol.one_away('pale', 'ple'))
print(sol.one_away('pales', 'pale'))
print(sol.one_away('pale', 'bale'))
print(sol.one_away('a', 'b'))
print(sol.one_away('pale', 'bake'))


