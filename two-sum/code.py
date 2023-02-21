class Solution:
    def twoSum(self, nums, target):
        # Create an empty dictionary to store the complements
        complements = {}
        
        # Traverse the array
        for i in range(len(nums)):
            # Check if the complement of the current element is already in the dictionary
            if target - nums[i] in complements:
                # If yes, return the indices of the current element and its complement
                return [complements[target - nums[i]], i]
            else:
                # If not, add the current element to the dictionary
                complements[nums[i]] = i
