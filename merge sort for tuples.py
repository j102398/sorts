def merge_sort_tuples(tuple_list, index):
  # Check if the length of the tuple_list is larger than 1, therefore needing sorting
  if len(tuple_list) > 1:
      # Split the list of tuples in half and store as two variables

      # This gets elements from start up until the middle
      LeftSideArray = tuple_list[0:len(tuple_list)//2]
      # This gets elements from the middle (including) until the end of the list of tuples
      RightSideArray = tuple_list[len(tuple_list)//2:len(tuple_list)]

      # Keep dividing the left and right-hand segments of the list of tuples until they don't need to be sorted anymore
      merge_sort_tuples(LeftSideArray, index)   # Recursive call to sort the left side
      merge_sort_tuples(RightSideArray, index)  # Recursive call to sort the right side

      # Put the bits back together to form the sorted list of tuples

      i = 0       # Left Array Index
      j = 0       # Right Array Index
      k = 0       # Original Array Index (this will be the sorted list of tuples)

      # Merging the two sorted halves into a single sorted list of tuples
      while i < len(LeftSideArray) and j < len(RightSideArray):
          if LeftSideArray[i][index] < RightSideArray[j][index]:
              tuple_list[k] = LeftSideArray[i]
              i += 1      # Incrementing as the value has already been sorted
          else:
              tuple_list[k] = RightSideArray[j]
              j += 1      # Incrementing as the value has already been sorted
          k += 1

      # Checking for any remaining elements in the left side
      while i < len(LeftSideArray):
          tuple_list[k] = LeftSideArray[i]
          i += 1
          k += 1

      # Checking for any remaining elements in the right side
      while j < len(RightSideArray):
          tuple_list[k] = RightSideArray[j]
          j += 1
          k += 1



### Example application
list_of_favourite_colours = [
    ("Blue", 74),
    ("Red", 32),
    ("Yellow", 23),
    ("Green", 123),
    ("Purple", 12),
    ("Brown", 22),
    ("White", 16),
    ("Grey", 1),
    ("Turqoise", 346),
    ("Orange", 12)
]


merge_sort_tuples(list_of_favourite_colours,1)
print(list_of_favourite_colours)
