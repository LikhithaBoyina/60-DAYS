def two_sum(nums, target):
    # Create a dictionary to store the index of each element
    num_dict = {}
    
    # Iterate over the list of numbers
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Store the index of the current number
        num_dict[num] = i

nums = list(map(int,input("Enter list of elements : ").split()))
target = int(input("Enter targeted number : "))
print(two_sum(nums, target))  

