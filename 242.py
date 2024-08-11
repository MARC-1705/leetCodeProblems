class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            #if the length of s and t are not equal, they cannot be anagrams
            return False
        #create a dictionary to store the frequency of each character in s and t
        charFreq = {}
        
        # fill the dictionary with the frequency of each character in s
        for char in s:
            charFreq[char] = charFreq.get(char, 0) + 1
        #check if the frequency of each character in t is the same as the 
        #frequency of the character in s
        for char in t:
            if char not in charFreq or charFreq[char] == 0:
                return False  
            charFreq[char] -= 1  
        
        #if the frequency of each character in t is the same as the frequency of 
        #the character in s return True
        return True
             