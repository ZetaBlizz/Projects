class Matrix(object):
    def __init__(self, matrix):
        self._matrix = matrix
        self._a1 = float(matrix[0][0]) #incase not already a float
        self._a2 = float(matrix[0][1])
        self._a3 = float(matrix[1][0])
        self._a4 = float(matrix[1][1])

    def __str__(self): #didn't name it M3 or M4 because of the guideline outputs
        return f'{[self._a1, self._a2]}\n{[self._a3, self._a4]}'

    def __mul__(self, other):
        return f'{[self._a1 * other, self._a2 * other]}\n{[self._a3 * other, self._a4 * other]}'
    
    def __rmul__(self, other):
        return f'{[self._a1 * other, self._a2 * other]}\n{[self._a3 * other, self._a4 * other]}'

    def __add__(self, M2):
        return f'{[self._a1 + M2._a1, self._a2 + M2._a2]}\n{[self._a3 + M2._a3, self._a4 + M2._a4]}'

    def __sub__(self, M2):
        return f'{[self._a1 - M2._a1, self._a2 - M2._a2]}\n{[self._a3 - M2._a3, self._a4 - M2._a4]}'

    def determinant(self):
        return float(self._a1 * self._a4 - self._a2 * self._a3)

    def trace(self):
        return float(self._a1 + self._a4)

    def inverse(self):
        D = self.determinant()
        if D == 0:
            return 'matrix is singular!'
        else:
            return f'{[self._a4/D, -1*self._a2/D]}\n{[-1*self._a3/D, self._a1/D]}'

    def characteristic_polynomial(self):
        return f'(x^2)-{self.trace()}*x+{self.determinant()}'

    def matrix_product(self, M2):
        return f'{[self._a1*M2._a1+self._a2*M2._a3, self._a1*M2._a2+self._a2*M2._a4]}\n' \
            f'{[self._a3*M2._a1+self._a4*M2._a3, self._a3*M2._a2+self._a4*M2._a4]}'

def checks(m1,m2): #Makes sure data passed to Class Matrix is formatted well
    first = []
    second = []
    final = []
    m1 = m1.split(",")
    m2 = m2.split(",")
    for i in m1:
        try: first.append(float(i))
        except:
            return "Please only use integers/floats"
    for i in m2:
        try: second.append(float(i))
        except:
            return "Please only use integers/floats"
    final.append(first)
    final.append(second)
    if len(m1) != len(m2):
       return "Make sure matrices are the same size"
    return final

if __name__ == '__main__':
    #---------------------ANSWERS--------------------------------------------
    
    M1 = Matrix([[2.0, -5.0], [8.0, 3.0]])
    M2 = Matrix([[-1.0, 1.0], [2.0, 3.0]])
    print(M1*M2)
    #[2.0, -5.0]
    #[8.0, 3.0]
    print(M2)
    #[-1.0, 1.0]
    #[2.0, 3.0]
    
    M1.determinant()
    #46.0
    M2.determinant()
    #-5.0
    
    M1.trace()
    #5.0
    M2.trace()
    #2.0
    
    M1.inverse()
    #[0.06521739130434782, 0.10869565217391304]
    #[-0.17391304347826086, 0.043478260869565216]
    M2.inverse()
    #[-0.6, 0.2]
    #[0.4, 0.2]
    
    M1.characteristic_polynomial()
    #(x^2)-5.0*x+46.0
    M2.characteristic_polynomial()
    #(x^2)-2.0*x+-5.0
    
    M1.matrix_product(M2)
    #[-12.0, -13.0]
    #[-2.0, 17.0]
    M2.matrix_product(M1)
    #[6.0, 8.0]
    #[28.0, -1.0]
    
    print(7*M1)
    #[14.0, -35.0]
    #[56.0, 21.0]
    print(M2*7)
    #[-7.0, 7.0]
    #[14.0, 21.0]
    
    print(M1+M2)
    #[1.0, -4.0]
    #[10.0, 6.0]
    print(M2+M1)
    #[1.0, -4.0]
    #[10.0, 6.0]
    
    print(M1-M2)
    #[3.0, -6.0]
    #[6.0, 0.0]
    print(M2-M1)
    #[-3.0, 6.0]
    #[-6.0, 0.0]
    
