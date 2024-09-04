class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #First solution
        # if len of nums is less than 2, return the length of nums
        # if len(nums) < 2: return len(nums)
        #define a dictionary to store the ocurrencies of the numbers
        # ocurrencyDict =  {}
        #define a variable to store the index of the next number to insert
        # insertIndex = 0
        #iterate over the nums list
        # for i in range(len(nums)):
        #     if the number is not in the dictionary of ocurrencies, insert the number in the insertIndex position
        #     increment the insertIndex and set the ocurrence of the number to True
        #     if nums[i] not in ocurrencyDict:
        #         nums[insertIndex] = nums[i]
        #         insertIndex += 1
        #         ocurrencyDict[nums[i]] =  True
            
        # return the insertIndex       
        
        # return insertIndex 
        
        
        #Second solution
        # define a variable to store the index of the last unique value starting from 0
        lastUniqueValueIndex = 0
        #iterate over the nums list starting from 1
        for i in range(1,len(nums)):
            #if the number is different from the last unique value, increment the lastUniqueValueIndex and
            # set the value of the lastUniqueValueIndex to the current number
            if(nums[i] != nums[lastUniqueValueIndex]):
                lastUniqueValueIndex += 1
                nums[lastUniqueValueIndex] = nums[i]
        #return the lastUniqueValueIndex + 1
        return lastUniqueValueIndex + 1 
        
        
        """
        Complexity analysis:
        Time: O(n) - always because we iterate over the nums list once
        
        Space: O(n) - in the first solution because we store the ocurrencies of the numbers in a dictionary
        Space: O(1) - in the second solution because we only store the index of the last unique value 
        
        """