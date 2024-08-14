class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #initialize a flag to check if we have encountered a character
        flag = False
        #initialize a counter to store the length of the last word
        counter = 0
        #iterate through the string from the end
        for i in range(len(s) -1,-1,-1):
            #if we encounter a character and the flag is set to True, return the counter
            if(flag and s[i] != " "):
                return counter
            #if we encounter a character and the flag is set to False, set the flag to True
            if(s[i] == " "):
                counter+=1
                flag = True
        return counter
            
        
            
            
            
            