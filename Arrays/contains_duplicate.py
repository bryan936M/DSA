class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Your implementation here
        
        #Declare a set(to not allow duplicates pre-emptively)
        unique_elements = set()
        
        #iterate thru the nums array, if an element doesn't exist add it to the set then continue, if it does return true
        for element in nums:
            if element in unique_elements:
                return True
            unique_elements.add(element)
        
        return False