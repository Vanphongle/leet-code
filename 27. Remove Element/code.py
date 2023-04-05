class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize pointers at the beginning of the array
        i = 0
        j = 0
        n = len(nums)
        
        # Iterate through the array
        while j < n:
            # If the current element is not equal to val, move it to the front of the array
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            # Move the second pointer to the next element
            j += 1
        
        # Return the number of elements that are not equal to val
        return i
