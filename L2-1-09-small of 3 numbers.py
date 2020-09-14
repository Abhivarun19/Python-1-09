#Find smallest number among three numbers

a = int(input())
b = int(input())
c = int(input())

if (a <= b) and (a <=c):
     print(a, "is small number") 
elif(b <= a and b <= c): 
    print(b, "is small number") 
else: 
    print(c, "is small number") 
