class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # We are going to create 3 pointers, one for the insert position,
        # one for the last element of nums1 and one for the last element of nums2
        # The insert position will be at the end of nums1, because we are going to
        # insert the elements from the end to the start.
        insertPosition = m + n - 1
        n1Index = m - 1
        n2Index = n -1 
        # We are going to iterate over the two arrays, placing the biggest element 
        # in the insert position and moving the pointer of the array that had the 
        # biggest element. We are going to do this until we reach the start of one 
        # of the arrays
        while(n1Index >= 0 and n2Index >= 0):
            if(nums2[n2Index] > nums1[n1Index]):
                nums1[insertPosition] = nums2[n2Index]
                n2Index -= 1
            else:
                nums1[insertPosition] = nums1[n1Index]
                n1Index -= 1
            
            insertPosition -= 1
        # If we reach the end of nums1, we need to insert the remaining
        # elements of nums2, we do not need to do this for nums1, because 
        # if it is the case that we hadn't inserted all the elements of nums1 
        # it means that they are already in the correct position
        
        while(n2Index >= 0):
            nums1[insertPosition] = nums2[n2Index]
            insertPosition -= 1
            n2Index -= 1
        
    #Time complexity analysis:
    # The time complexity of this algorithm is O(n+m) because we are going 
    # to iterate over the two arrays, and we are going to do it only once
    
    #Space complexity analysis:
    # The space complexity of this algorithm is O(1) because we are not using
    # any extra space, we are only using the space of the input arrays and some 
    # constant space variables as pointers
    
    

