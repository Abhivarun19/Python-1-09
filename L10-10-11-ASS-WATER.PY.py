'''A water reservation system constructed in a city has several opening
and closing gates. If any opening gates are not closed with a corresponding
closing gate then the water will leak out of the system and there will be a
threat to the life of people living in the city. Also, the closing gate cannot
exist without the opening gate, so the system head checks the design of the
system and he has to ensure that the people are safe in the city. Write an
algorithm to find whether people are safe or not.'''

A = input("Enter the string: ")
flag = 1
count = 0
stack = []
for x in A:
   if x == "(":
       stack.append(x)
   if x == ")":
       if stack == []:
           flag = 0
           break
       Y = stack.pop()
       if Y != "(":
           flag = 0
           break
       else:
           count = count+1            
if flag == 1:
   print("Count: %d" %(count))
else:
   print("-1")

