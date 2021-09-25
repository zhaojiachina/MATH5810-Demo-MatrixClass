class MyMatrix:
    def __init__(self, A):
        """
        To be consistent with code already written, it is
        being assumed that the matrix A (which was used
        because it is a common name for a 'general'  matrix
        in linear algebra) is a 2-D array, or nested list
        """
        self.A = A
  
    def __str__(self):
        pass
  
    def __mul__(self, A, B):
        """
        Takes in two MyMatrix objects A and B.
        Returns AB as a MyMatrix object. I found it made the most
        sense to code this by transposing B and then simply dotting
        the rows of A and B^T, but if there's a more efficient
        way that would be ideal.
        """
        if len(A[0]) != len(B):
            return None

        ab = [[0 for j in range(len(B[0]))] for i in range(len(A))]
        bt = self.transpose(B)

        for i in range(len(A)):
            for j in range(len(bt)):
                ab[i][j] = self._dot(A[i], bt[j])

        return MyMatrix(ab)
  
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

    def __len__(self):
        return len(self.A)

    def __getitem__(self, row):
        return self.A[row]

    def transpose(self, A):
        """
        Takes in A, a MyMatrix object.
        Returns the transpose of A as a MyMatrix object.
        """
        at = [[0 for j in range(len(A))] for i in range(len(A[0]))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                at[j][i] = A[i][j]

        return MyMatrix(at)

    def _dot(self, a, b):
        """
        Returns the dot product of two vectors (represented
        as 1-D arrays or lists). Used primarily in matrix
        multiplication in the MyMatrix class, and so it's been
        made 'private' as this isn't a MyVector class.
        """
        ab = 0
        for i in range(len(a)):
            ab += (a[i] * b[i])

        return ab
