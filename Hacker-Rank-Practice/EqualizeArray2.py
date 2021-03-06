

# PROBLEM
# Karl has list of integers, what he want to do is reduce the list so that all of the numbers left are equal to each other. By doing that we would have to determine the min numbers to delete in the list. For example, if his list consists of 1, 2, 2, 3; we could delete the numbers 1 and 3, leaving inside the list 2, 2; or we could delete the numbers 2 and 2, and either 1 or 3 but that would be 3 deletions and the min number of deletions will be 2. We need to return the min number of deletions, which in the example is 2.

# HIGH LEVEL SOLUTION:
# Look through the list and store each element in a dictionary counting any duplicates. Look in the dictionary and find the element with the largest count value. Subtract that largest value from the length of the original list and return the min number of deletions.

# SOLUTION:
# Step 1: Set a counter to zero, to count the number of equal elements from the given array.
# Step 2: Create an Elements dictionary to store the given array's key value pairs.
# Step 3: Loop through the array, arr, to find the elements that are equal to eachother.
# Step 4: Check if the element of i is not in the Elements dictionary, then move onto the next element of the array at index j.
# Step 5: Check if element of i is equal to element of j, then increment the counter.
# Step 6: Add the count to the Elements dictionary
# Step 7: Find the key with the largest value.
# Step 8: Return the min number of deletions by subtracting the largest value from the length of the original array.

# The Runtime: O(n^2)(squared) because we have 2 for loops that are nested together. 

def equalizeArray(arr):
    # Set a counter to zero, to count the number of equal elements from the given array.
    count = 0
    # Create an Elements dictionary to store the given array's key value pairs.
    Elements = {}

    # Loop through the array, arr, to find the elements that are equal to eachother.
    for i in arr:
        # Check if the 1st index is not in the Elements dictionary, then move onto the next index of the array.
        if i not in Elements:
            for j in arr:
                # Check if 1st index is equal to the second index, if it is, then increment the counter.
                if i == j:
                    count= count+1
            # Add the count to the Elements dictionary
            Elements[i] = count
            count = 0

    # Find the key with the largest value.
    max_val = max(Elements, key= Elements.get)

    # Return the min number of deletions by subtracting the largest value from the length of the original array.
    return (len(arr) - Elements[max_val])


## Faster Runtime solution:

def equalizeArray(arr):
  # variable tracking how many times the most-used value appears in arr
  maxDuplicates = 0

  # dict for storing how many times each value appears in arr
  Elements = {}
​
  # loop through arr
  for i in arr:
    # if i is not in our dict, it means we haven't encountered it yet
    if i not in Elements:
      # so we make the value 1 in the dict
      Elements[i] = 1
    # if we HAVE encountered it  
    else:
      # increase the counter in the dict
      Elements[i] += 1
​
    # check to see if our new value in the dict is bigger than maxDuplicates
    # if it is, that means this value in arr is (for now) more frequent than other values
    if Elements[i] > maxDuplicates:
      # so we assign maxDuplicates to this new counter value
      maxDuplicates = Elements[i]
  
  # the minimum number of deletions is going to equal the length of the array minus the number of times the most common value appears
  return len(arr) - maxDuplicates