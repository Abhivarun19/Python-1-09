#copy the contents from one array to another array in reverse order

#intializing array
arr1 = [1,2,3,4,5]

arr2 = [None]*len(arr1)
length = len(arr1)
#copying elements
for i in range(0,length):
        arr2[i]=arr1[length-i-1]

#display the elements
print("elements of first array")
print(arr1)

#display the elements of new array
print("elements of new array")
for i in range(0,len(arr2)):
print(arr2[i])
