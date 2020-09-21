#MATRIX TO SPARCE MATRIX
#Function1(For dispalying matrix)
def dispmatrix(a):
    for row in matrix:
        for ele in row:
            print(ele, end=" ")
        print()
#Function2(For converting to sparse matrix)
def sparse(a):
    sparseMatrix = []
    Threshold=int(input("Enter threshold value:"))
    for i in range(len(matrix)):
        for j in range(len(matrix[2])):
            if (matrix[i][j]<=Threshold):
                matrix[i][j]=0
            if(matrix[i][j]!=0):
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
                sparseMatrix.append(temp)
       print()
    #output
    print("SparseMatrix:")
    for row in sparseMatrix:
        for ele in row:
            print(ele, end=" ")
        print()
#Input
row1 = int(input("Enter the number of rows:"))
col1 = int(input("Enter the number of columns:"))
#Initialize matrix
matrix = []
print("Enter the entries rowwise:")
for i in range(row1):
    a = []
    for j in range(col1):
        a.append(int(input()))
    print()
    matrix.append(a)
dispmatrix(matrix)#Calling Funtion1
sparse(matrix)#Calling Fuction2
