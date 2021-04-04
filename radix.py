# Using counting sort to sort the elements based on significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    print("count:"+str(count))

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    print("count(summation):"+str(count))

    # Place the elements in sorted orderd
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

    print("array:"+str(array) + "\n")


# Main function of radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    print("\nmaximum number: "+str(max_element))

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [84, 23, 62, 44, 16, 30, 95, 51,16,59]
print("Input is:")
print(data)
radixSort(data)
print("Output is:")
print(data)