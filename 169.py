class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #First solution
        # if len of nums is less than 3, return yhe first element of nums
        if len(nums) < 3: return nums[0]
        
        #Calculate the majority factor
        majorityFactor = len(nums) // 2
        #Create a dictionary to store the ocurrencies of the numbers 
        ocurrencyDict = {}
        #Iterate over the nums list
        for num in nums:
            #If the number is not in the dictionary of ocurrencies, insert the number in the dictionary
            ocurrencyDict[num] = ocurrencyDict.get(num, 0) + 1
            #If the ocurrence of the number is higher than the majority factor, return the number
            if(ocurrencyDict.get(num,0) > majorityFactor):
                return num
        
        
        #Moore solution
        
        # count = 0
        # ans = -1

        # for num in nums:
        #     if(count == 0):
        #         ans = num
        #     if(ans == num):
        #         count += 1
        #     else:
        #         count -= 1
        
        # return ans
        
        
"""
Complexity analysis:

Fist solution:
Time: O(n) - always because we iterate over the nums list once
Space: O(n) - because we store the ocurrencies of the numbers in a dictionary

Second solution:
Time: O(n) - always because we iterate over the nums list once
Space: O(1) - because we only store the count and the ans


"""