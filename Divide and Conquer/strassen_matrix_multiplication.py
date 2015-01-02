"""
Strassen Subcubic Matrix Multiplication
An efficient matrix multiplication algorithm based on the Divide and Conquer paradigm.
Performs multiplication in subcubic time by reducing the number of products calculated.

Input is given in 'Matrix Input.txt' file.
(Done) Object Oriented approach with Operator Overloading to simplify the code.
"""


class Matrix(object):
    """
    Uses a list of lists to construct a Matrix.
    Includes operator overloading.
    """
    def __init__(self, list_of_lists):
        # take a list of lists to initialize the matrix
        self.value = list_of_lists
        self.dim = len(list_of_lists)

    def __str__(self):
        # pretty print the matrix
        formatted = ""
        for i in range(self.dim):
            formatted += ("[\t" + "\t".join(map(str, self.value[i])) + "\t]\n")
        return formatted

    def __repr__(self):
        return 'Matrix\nDim: %d\nValue: %s' % (self.dim, str(self))

    def __add__(self, other):
        # overload the + operator for matrix addition
        mat = []
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                row.append(self.value[i][j] + other.value[i][j])
            mat.append(row)
        return Matrix(mat)

    def __sub__(self, other):
        # overload the - operator for matrix subtraction
        mat = []
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                row.append(self.value[i][j] - other.value[i][j])
            mat.append(row)
        return Matrix(mat)

    def __mul__(self, other):
        # overload the * operator for matrix multiplication
        return strassen_multiplication(self, other)


def create_submatrix(matrix, row_lower, row_upper, col_lower, col_upper):
    """
    create a submatrix from a larger one, given the bounds for row and column.
    """
    sub_mat = []
    for i in range(row_lower, row_upper):
        row = []
        for j in range(col_lower, col_upper):
            row.append(matrix.value[i][j])
        sub_mat.append(row)
    return Matrix(sub_mat)


def strassen_multiplication(matrix_one, matrix_two):
    """
    Strassen's subcubic multiplication function. Takes two matrices and returns their product matrix.
    """
    # Base case, return integer product.
    if matrix_one.dim == 1:
        return matrix_one.value[0][0] * matrix_two.value[0][0]

    # Create submatrices
    submatrix_a = create_submatrix(matrix_one, 0, matrix_one.dim / 2, 0, matrix_one.dim / 2)
    submatrix_b = create_submatrix(matrix_one, 0, matrix_one.dim / 2, matrix_one.dim / 2, matrix_one.dim)
    submatrix_c = create_submatrix(matrix_one, matrix_one.dim / 2, matrix_one.dim, 0, matrix_one.dim / 2)
    submatrix_d = create_submatrix(matrix_one, matrix_one.dim / 2, matrix_one.dim, matrix_one.dim / 2, matrix_one.dim)

    submatrix_e = create_submatrix(matrix_two, 0, matrix_two.dim / 2, 0, matrix_two.dim / 2)
    submatrix_f = create_submatrix(matrix_two, 0, matrix_two.dim / 2, matrix_two.dim / 2, matrix_two.dim)
    submatrix_g = create_submatrix(matrix_two, matrix_two.dim / 2, matrix_two.dim, 0, matrix_two.dim / 2)
    submatrix_h = create_submatrix(matrix_two, matrix_two.dim / 2, matrix_two.dim, matrix_two.dim / 2, matrix_two.dim)

    # Perform recursive multiplications
    product_1 = submatrix_a * (submatrix_f - submatrix_h)
    product_2 = (submatrix_a + submatrix_b) * submatrix_h
    product_3 = (submatrix_c + submatrix_d) * submatrix_e
    product_4 = submatrix_d * (submatrix_g - submatrix_e)
    product_5 = (submatrix_a + submatrix_d) * (submatrix_e + submatrix_h)
    product_6 = (submatrix_b - submatrix_d) * (submatrix_g + submatrix_h)
    product_7 = (submatrix_a - submatrix_c) * (submatrix_e + submatrix_f)

    # Wrapping up, putting it all together
    # Final Terms
    submatrix_ae = product_5 + product_4 - product_2 + product_6
    submatrix_bf = product_1 + product_2
    submatrix_cg = product_3 + product_4
    submatrix_dh = product_1 + product_5 - product_3 - product_7

    # Combine sub matrices to form elements of result matrix
    product_matrix = []
    for i in range(matrix_one.dim):
        product_matrix.append([])
        for j in range(matrix_two.dim):
            if i < matrix_one.dim / 2:
                if j < matrix_two.dim / 2:
                    product_matrix[i].append(
                        submatrix_ae.value[i][j] if type(submatrix_ae) is not int else submatrix_ae)
                else:
                    product_matrix[i].append(
                        submatrix_bf.value[i][j - matrix_two.dim / 2] if type(submatrix_bf) is not int else submatrix_bf)
            else:
                if j < matrix_two.dim / 2:
                    product_matrix[i].append(
                        submatrix_cg.value[i - matrix_one.dim / 2][j] if type(submatrix_cg) is not int else submatrix_cg)
                else:
                    product_matrix[i].append(
                        submatrix_dh.value[i - matrix_one.dim / 2][j - matrix_two.dim / 2] if type(submatrix_dh) is not int else submatrix_dh)
    return Matrix(product_matrix)


def main():
    """
    main function
    """
    infile = open("Matrix Input.txt", "r")
    order = int(infile.readline())

    # Take in first matrix.
    list_of_lists = []
    for i in range(order):
        row = [int(num) for num in infile.readline().split(' ')]
        list_of_lists.append(row)
    matrix_one = Matrix(list_of_lists)
    print matrix_one

    print "multiplied by\n"

    # Take in second matrix.
    list_of_lists = []
    for i in range(order):
        row = [int(num) for num in infile.readline().split(' ')]
        list_of_lists.append(row)
    matrix_two = Matrix(list_of_lists)
    print matrix_two

    print "equals\n"

    product_matrix = matrix_one * matrix_two
    print product_matrix

if __name__ == "__main__":
    main()
