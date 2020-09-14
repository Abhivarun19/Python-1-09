#Delete the duplicate elements from an array

def Remove(dup): 
    final=[] 
    for num in dup: 
        if num not in final: 
            final.append(num) 
    return final 
dup = [1,3,4,5,9,4,3,7,8,9] 
a=Remove(dup) 
print("elements of the array after removing duplicates is")
for i in range(0,len(a)):
    print(a[i])
print("and array is:",a)
