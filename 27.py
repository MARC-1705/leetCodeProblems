class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # We are going to iterate over the array from the end to the start, 
        # we are going to keep track of the index where we are going to insert
        # the elements that are not equal to val, starting from the end of the array
        insertIndex =  len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            #if the element is equal to val, we are going to replace 
            #it with the element that is in the insertIndex and decrease
            #the insertIndex
            if(nums[i] == val):
                nums[i] = nums[insertIndex]
                insertIndex -= 1
             
        #The insertIndex is going to be the index of the last element that
        #is not equal to val and we add 1 to get the numnber of elements that
        #are not equal to val
        
        return insertIndex + 1