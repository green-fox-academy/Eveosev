"""
   Matrix Operations:
"""
#Addtion
def matrixadd(A,B):
    added = []
    for i in range(len(A)):
        eachrow = []
        for j in range(len(A[0])):
            eachrow.append(A[i][j] + B[i][j])
        added.append(eachrow)
    return added

#eample
a = [[1,6],
     [3,4]]
b = [[2,1],
     [4,5]]
matrixadd(a,b)

#Substraction
def matrixminus(A,B):
    minus = []
    for i in range(len(A)):
        eachrow = []
        for j in range(len(A[0])):
            eachrow.append(A[i][j] - B[i][j])
        minus.append(eachrow)
    return minus

#eample
a = [[1,6],
     [3,4]]
b = [[2,1],
     [4,5]]
matrixminus(a,b)

#Scalar multiplication
def scalar_multiplication(a, B):
    sm_matrix = []
    for i in range(len(B)):
        eachrow = []
        for j in range(len(B[0])):
            eachrow.append(B[i][j] * a)
        sm_matrix.append(eachrow)
    return sm_matrix

scalar_multiplication(2, b)

#Transposition
def transposition(X):
    for i in range(1, len(X)):
        for j in range(i):
            X[i][j], X[j][i] = X[j][i], X[i][j]
    return X
"""
example:
"""
a = [[1,6],
     [3,4]]
Ta = transposition(a)
print(f"The transposition of {a} is {Ta}")

#Matrix multipilication
def matrixtimes(A, B, C = []):
  for i in range(len(A)):
      colsum = []
      for j in range(len(B[0])):
          temp = 0
          for k in range(len(A[0])):
              temp = temp + A[i][k] * B[k][j]
          colsum.append(temp)
      C.append(colsum)
  return C
matrixtimes(a, b)

#Vertical flipping
def verticalflip(A):
    n = len(A)
    if n % 2 == 0:
        for i in range(n // 2):
            A[i], A[n- 1 - i] = A[n - 1 - i], A[i]
    else:
        for i in range( (n - 1) // 2):
            A[i], A[n - 1 -i] = A[n - 1 - i], A[i]
    return(A)

verticalflip(a)

#Main anti diagonal mirroring
def antidiagonalT(X):
    n = len(X)
    for i in range(len(X)):
        for j in range(n - 1 - i):
            X[i][j], X[n - 1 - j][n - 1 - i] = X[n - 1 - j][n - 1 - i], X[i][j]
    return X
"""
example:
"""
a = [[1,6],
     [3,4]]
antiTa = antidiagonalT(a)
print(f"The anti diagonal of {a} is {antiTa}")

#Horizonal flipping
def horizonalflip(X, hf_X = []):
    for i in X:
      hf_X.append(i[::-1])
    return hf_X

"""
example:
"""
a = [[1,6],
     [3,4]]
hf_a = horizonalflip(a)
print(f"The anti diagonal of {a} is {hf_a}")
   
#Matrix rotation
def matrixrotate(X):
    row = len(X)
    column = len(X[0])
    rotated = []
    for i in range(column):
        rotated.append([])
    for i in range(row):
        for j in range(column):
            rotated[column - 1 - j].append(X[i][j])
    return rotated
"""
example:
"""
a_mt = [[1,6,3],
        [3,4,5]]
mt_a = matrixrotate(a_mt)
print(f"The rotated matrix of {a_mt} is {mt_a}")
  
#Extended matrix rotation ( in any situation of any multiplication of 90 degree )
def multimatrixrotate(X, degree):
    multi = (degree // 90) % 4
    for k in range(multi):
        X = matrixrotate(X)
    return X      
"""
example:
"""
a_multi = [[1,6,3],
           [3,4,5]]
degree = 270
mulitmt_a = multimatrixrotate(a_multi, degree)
print(f"The {degree} degree rotated matrix of {a_multi} is {mulitmt_a}")






































