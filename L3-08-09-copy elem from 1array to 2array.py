#copy the contents from one array to another array

#intializing array
arr1 = [1,2,3,4,5]

arr2 = [None]*len(arr1)
#copying elements
for i in range(0,len(arr1)):
               arr2[i]=arr1[i]

#display the elements
print("elements of first array")
for i in range(0,len(arr1)):
        print(arr1[i])

#display the elements of new array
print("elements of new array")
for i in range(0,len(arr2)):
        print(arr2[i])
    
