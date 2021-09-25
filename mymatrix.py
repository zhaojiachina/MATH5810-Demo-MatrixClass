import math

class MyMatrix:
  def __init__(self):
    pass

  def __init__(self, A):
      """
      A is the input matrix
      """
      self.A = A
  
  def __str__(self):
    pass
  
  def __mul__(self):
    pass
  
  def __add__(self, x, y):
    """
    x, y are MyMatrix object, the return is also MyMatrix object.
    here, I assume __getitem__ is defined
	here, I assume the init of MyMatrix using the nested list,
	which is like this [[], []]
    """
    sums = []
    for i in range(len(x)):
    	row = []
    	for j in range(len(y)):
    		# row.append(x.index(i, j) + y.index(i, j))
    		row.append(x[i][j] + y[i][j])
    	sums.append(row)

    return MyMatrix(sums)

  def norm1(self):
      """
      A is MyMatrix object which is a list in the form [[],[],[]]
      The method returns the 1-norm of matrix A, ||A||_1, which is a number
      The formula to calculate 1 norm of a matrix is ||A||_1 = max_{1<=j<=n} sum_{i=1^m} |a_{ij}|
      which is maximum absolute column sum of the matrix
      Example: input: A = MyMatrix([[1,2,3],[4,5,6]])
               return: A.norm1() = 9
      """
      matrix_norm1 = 0

      for j in range(0,len(self.A[0])):#the number of columns
          column_sum = 0
          for i in range(0,len(self.A)):#the number of rows
             column_sum += abs(self.A[i][j])
          if matrix_norm1 < column_sum:
              matrix_norm1 = column_sum
          else:
              continue

      return matrix_norm1

  def norm_infinity(self):
      """
      A is MyMatrix object which is a list in the form [[],[],[]]
      The method returns the infinity-norm of matrix A, ||A||_∞, which is a number
      The formula to calculate infinity norm of a matrix is ||A||_∞ = max_{1<=i<=n} sum_{j=1^n} |a_{ij}|
      which is maximum absolute row sum of the matrix
      Example: input: A = MyMatrix([[1,2,3],[4,5,6]])
               return: A.norm_infinity() = 15
      """

      matrix_norm_infinity = 0

      for i in range(0, len(self.A)):
          row_sum = 0
          for j in range(0, len(self.A[0])):
              row_sum += abs(self.A[i][j])
          if matrix_norm_infinity < row_sum:
              matrix_norm_infinity = row_sum
          else:
              continue

      return matrix_norm_infinity

  def normF(self):
      """
      A is MyMatrix object which is a list in the form [[],[],[]]
      The method returns the Frobenius norm of matrix A, ||A||_F, which is a number
      The formula to calculate the Frobenius norm of a matrix is ||A||_F = sqrt(sum_{1<=i<=n} (sum_{j=1^n} |a_{ij}|^2))
      Example: input: A = MyMatrix([[1,0,1],[1,2,0]])
               return: A.normF() = sqrt(7)
      """

      matrix_normF = 0

      for i in range(0, len(self.A)):
          for j in range(0, len(self.A[0])):
              matrix_normF += abs(self.A[i][j])**2

      return math.sqrt(matrix_normF)


 
