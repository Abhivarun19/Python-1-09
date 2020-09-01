#GCD and LCM of two numbers
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))

#logic for GCD
if(a<b) and (a<c):
    small=a
elif(b<a) and (b<c):
    small=b
else:
    small=c
for i in range(1,small+1):
    if(a%i==0 and b%i==0 and c%i==0):
        gcf=i

#logic for LCM
lcm=(a*b*c)/gcf

#Displaying GCD nad LCM of two numbers
print("GCM of a and b and c is",gcf)
print("LCM of a and b and c is",lcm)
