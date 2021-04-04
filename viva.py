
A = [84,23,62,44,16,30,95,51,16,100]

minimum = int(min(A)) #find minimum value of array
highest = int(max(A)) #find highest value of array

counter = [0]*(highest-minimum+1) #create and initialize counter array as 0
output = [0]*(len(A)) # create and initialize output array as 0

for i in range (0,len(A)):
     counter[A[i]-minimum] += 1 #store count for each number
print(f"storing count \n {counter} ")
for i in range(1, len(counter)):
       counter[i] += counter[i-1] #modify counter array by adding previous count
print(f"doing summation \n {counter} ")
for i in range(len(A)-1, -1, -1):
        output[counter[A[i] - minimum] - 1] = A[i] #add the actual sorted number into output array
        counter[A[i] - minimum] -= 1
print(f"array counter after sorting \n{counter} \nsorted array \n{output}")


