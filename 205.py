class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Start with two empty dictionaries to map characters from s to t and from t to s
        charMap_s_to_t = {}
        charMap_t_to_s = {}
        # Iterate over the characters of s and t
        for i in range(len(s)):
            # If the character s[i] is already mapped to a character different from t[i] or
            # if the character t[i] is already mapped to a character different from s[i],
            # then the strings are not isomorphic
            if (s[i] in charMap_s_to_t and charMap_s_to_t.get(s[i]) != t[i] or 
                t[i] in charMap_t_to_s and charMap_t_to_s.get(t[i]) != s[i]
                ): return False 
            # Otherwise, map the characters s[i] and t[i]
            charMap_s_to_t[s[i]] = t[i]
            charMap_t_to_s[t[i]] = s[i]
            
        # If the strings are isomorphic, return True
        return True 
    
    
    """
    Time complexity: O(n), where n is the length of the strings s and t
    Space complexity: O(n), where n is the length of the strings s and t
    """
    
    