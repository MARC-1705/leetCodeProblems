class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Create a dictionary to store the frequency of each character in the magazine
        charFreq = {}
        # Count the frequency of each character in the magazine
        for char in magazine:
            charFreq[char] =  charFreq.get(char,0) + 1
        # Check if the ransomNote can be constructed from the magazine, by checking if the frequency of each character in 
        # the ransomNote is less than or equal to the frequency of the character in the magazine, if not return False
        for char in ransomNote:
            if not charFreq.get(char, 0) :
                return  False
            else: 
                charFreq[char] = charFreq.get(char,0) - 1
        # If the ransomNote can be constructed from the magazine, return True
        return True
    
    """
    Time Complexity: O(n):
        It has a complexity of O(n) because we iterate through the magazine to count the frequency of each
        character in the magazine and then iterate through the ransomNote to check if the ransomNote can be constructed, 
        so we have a complexity of O(n) + O(n) = O(n) 
    Space Complexity: O(n):
        We use a dictionary to store the frequency of each character in the magazine, so we have a space complexity of O(n)
    
    
    """
    