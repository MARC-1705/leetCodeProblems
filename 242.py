class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            #if the length of s and t are not equal, they cannot be anagrams
            return False
        #create a dictionary to store the frequency of each character in s and t
        charFreq = {}
        
        for char in s:
            charFreq[char] = charFreq.get(char, 0) + 1
        
        for char in t:
            if char not in charFreq or charFreq[char] == 0:
                return False  
            charFreq[char] -= 1  
        
        
        return True
             