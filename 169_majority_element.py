class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the majority element and its count.
        majority_element = nums[0]
        count = 1
        
        # Iterate through the array starting from the second element.
        for i in range(1, len(nums)):
            # If the count becomes zero, update the majority element to the current element.
            if count == 0:
                majority_element = nums[i]
                count = 1
            # If the current element is the same as the majority element, increment the count.
            elif nums[i] == majority_element:
                count += 1
            # If the current element is different, decrement the count.
            else:
                count -= 1
        
        return majority_element
