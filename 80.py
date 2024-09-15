class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if the lenght of nums is less than 2 return the lenght of nums
        if(len(nums) < 2):
            return len(nums)    
        
        #initialize the insert position to 2, because we know that 
        #the first two elements are at most repeated twice
        insertPosition = 2   
        
        #we iterate over the nums list starting from the third element
        for currentIndex in range (2, len(nums)):
            #if the current element is different from the element at the position
            #insertPosition - 2, we insert the current element in the insertPosition
            #and increment the insertPosition
            #it is insertPosition - 2 because the elements are at most repeated twice
            #so we have to check the element two positions before the insertPosition
            
         
            if(nums[currentIndex] != nums[insertPosition - 2]):
                nums[insertPosition] = nums[currentIndex]
                insertPosition += 1
        #return the insertPosition
        return insertPosition
    
    
    """
    Complexity analysis:
    Time: O(n) - always because we iterate over the nums list once
    Space: O(1) - because we only store the insertPosition
    """

    