#implementing linear search
def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = [ 1, 2, 4, 6, 8, 12, 15, 18, 20, 25, 30, 35, 40]
x = 25
print("element found at index "+str(linear_search(arr,x)))
