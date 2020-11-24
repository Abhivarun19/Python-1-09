def insertionSort(array):

    for x in range(1, len(array)):
        key = array[x]
        j = x - 1       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

l=[]
n = int(input("enter size:"))
for x in range(n):
   l.append(int(input("enter elements:")))
print("list:",l)
insertionSort(l)
print('Sorted Array in Ascending Order:')
print("list:",l)
