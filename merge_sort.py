
def merge_sort(array):
    # Check if the length of the array is larger than 1, therefore needing sorting
    if len(array) > 1:
        # Split the array in half and store as two variables

        # This gets elements from start up until the middle
        LeftSideArray = array[0:len(array)//2]
        # This gets elements from the middle (including) until the end of the array
        RightSideArray = array[len(array)//2:len(array)]

        # Keep dividing the left and right-hand segments of the array until they don't need to be sorted anymore
        merge_sort(LeftSideArray)   # Recursive call to sort the left side
        merge_sort(RightSideArray)  # Recursive call to sort the right side

        # Put the bits back together to form the sorted array

        i = 0       # Left Array Index
        j = 0       # Right Array Index
        k = 0       # Original Array Index (this will be the sorted array)

        # Merging the two sorted halves into a single sorted array
        while i < len(LeftSideArray) and j < len(RightSideArray):
            if LeftSideArray[i] < RightSideArray[j]:
                array[k] = LeftSideArray[i]
                i += 1      # Incrementing as the value has already been sorted
            else:
                array[k] = RightSideArray[j]
                j += 1      # Incrementing as the value has already been sorted
            k += 1

        # Checking for any remaining elements in the left side
        while i < len(LeftSideArray):
            array[k] = LeftSideArray[i]
            i += 1
            k += 1

        # Checking for any remaining elements in the right side
        while j < len(RightSideArray):
            array[k] = RightSideArray[j]
            j += 1
            k += 1

