import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            res = self.g[0][0]
        else:
            res = self.g[0][0] * self.g[1][1] - self.g[1][0] * self.g[0][1]
        
        return res

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        res = 0
        for i in range(self.h):
            res = res + self.g[i][i]
            
        return res

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        res = []
        if self.h == 1 :
            res.g.append([1/self.g])
        else:
            scalar = 1 / (self.g[0][0] * self.g[1][1] - self.g[1][0] * self.g[0][1])
            row_1 = [scalar*self.g[1][1], -scalar*self.g[0][1]]
            row_2 = [-scalar*self.g[1][0], scalar*self.g[0][0]]
            res.append(row_1)
            res.append(row_2)
         
        return Matrix(res)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for i in range(self.w):
            temp = []
            for j in range(self.h):
                temp.append(self.g[j][i])
            matrix_transpose.append(temp)
    
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
    
        # matrix to hold a row for appending sums of each element
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[0])):
                row.append(self.g[i][j] + other.g[i][j])
            matrixSum.append(row)
        
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        res = []
        for i in range(len(self.g)):
            temp = []
            for j in range(len(self.g[0])):
                temp.append(-self.g[i][j])
            res.append(temp)
        
        return Matrix(res)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        res = []
    
        # matrix to hold a row for appending sums of each element
        for i in range(len(self.g)):
            temp = []
            for j in range(len(self.g[0])):
                temp.append(self.g[i][j] - other.g[i][j])
            res.append(temp)
        
        return Matrix(res)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        res = []
        
        other_T = []
        for i in range(other.w):
            temp = []
            for j in range(other.h):
                temp.append(other[j][i])
            other_T.append(temp)
            
        for i in range(len(self.g)):
            temp = []
            for j in range(len(other_T)):
                val = 0
                for k in range(len(self.g[0])):
                    val = val + self.g[i][k] * other_T[j][k]
                temp.append(val)
            res.append(temp)
        
        return Matrix(res)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            res = []
            for i in range(len(self.g)):
                temp = []
                for j in range(len(self.g[0])):
                    temp.append(other * self[i][j])
                res.append(temp)
            
            return Matrix(res)
            