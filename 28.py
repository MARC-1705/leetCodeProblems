class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      
        #Initialize two pointes, one por the haystack, other for the needle
        haystackPointer = 0 
        needlePointer = 0
        
        "0 1 2 3 4 5 6 7"
        "l e e t c o d e " "len = 8"
        "        c o d e"  "len = 4"
        "8 - 4 >= 4"
        "len(haystack) - haystackPointer >= len(needle)"

        
        #Start the cycle that will advance the pointers depending on the  case, it should
        #go continue while is not at the final position of the haystack and while  it fullfill:
        #len(haystack) - haystackPointer >= len(needle) based on the top logic 
        while(haystackPointer< len(haystack) and (len(haystack) - haystackPointer) >= len(needle)):
            #if there is a match between the correspondings chars we increase the needle pointer
            if(haystack[haystackPointer + needlePointer] == needle[needlePointer]):
                needlePointer+=1
                if(needlePointer >= (len(needle))):
                    #if the needlePointer is higher or equal to the len of needle, meaning
                    #that we have a complete match return the haystack pointer
                    return haystackPointer
            else:
                #if there exist a missmatch we have to reset the needle pointer and 
                #advance the haystack pointer
                needlePointer = 0
                haystackPointer += 1
        
        #if we couldn't find a coincidence return -1
        return -1


     #Most common solution
    # def strStr(self, haystack, needle):
    #     for i in range(len(haystack) - len(needle) + 1):
    #         if haystack[i:i+len(needle)] == needle:
    #             return i
    #     return -1
    
    """
    Time complexity analysis of both algoritms:
        1-in the worst case is going to be O(n*m) because it will make m comparisions 
         of the lenght of the needle in each haystack position
        2-In the worst case is going to be O((m-n+1)*n) because the first for has a O(m-n+1)
         complexity and the slicing and comparition each has O(n), if m>>n we can say that has 
         a complexity of O(m*n)
         
    Space complexity analysis:
        1- The first one has a O(1) space complexity because it only uses space constant
         variables 
        2- The second one has O(n) space complexity the analized sub-strings where n is the
         lenght of needle
    """
    