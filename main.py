arr = [10,8,3,2,1]

def insertion_sort(arr):

    n = len(arr)

    for i in range(1, n):

        # Define the value to be inserted
        value = arr[i]

        # Define the maximum bound of the sorted sub-array
        j = i-1

        # Compare value with each element on sub-array, going left from the max-bound until a lesser element is found
        # Or until the end of the sub array.
        while j >= 0 and value < arr[j]:
            #Move the higher value one position ahead
            arr[j+1] = arr[j]
            #Go left
            j-=1

        # Place value at after the element which is smaller and thus stopped the while loop
        arr[j+1] = value

insertion_sort(arr)
print(arr)
