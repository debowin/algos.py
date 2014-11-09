# Strassen Subcubic Matrix Multiplication
# An efficient matrix multiplication algorithm based on the Divide and Conquer paradigm.
# Performs multiplication in subcubic time by reducing the number of products calculated.

# Input is given in 'Matrix Input.txt' file.
# (Done) Object Oriented approach with Operator Overloading to simplify the code.

class Matrix(object):
	def __init__(self, list_of_lists):
		# take a list of lists to initialize the matrix
		self.value = list_of_lists
		self.dim = len(list_of_lists)

	def __str__(self):
		# pretty print the matrix
		formatted = ""
		for i in range(self.dim):
			formatted+=("[\t"+"\t".join(map(str,self.value[i]))+"\t]\n")
		return formatted

	def __repr__(self):
		return 'Matrix\nDim: %d\nValue: %s' %(self.dim,str(self))

	def __add__(self, other):
		# overload the + operator for matrix addition
		mat = []
		for i in range(self.dim):
			row = []
			for j in range(self.dim):
				row.append(self.value[i][j]+other.value[i][j])
			mat.append(row)
		return Matrix(mat)

	def __sub__(self, other):
		# overload the - operator for matrix subtraction
		mat = []
		for i in range(self.dim):
			row = []
			for j in range(self.dim):
				row.append(self.value[i][j]-other.value[i][j])
			mat.append(row)
		return Matrix(mat)

	def __mul__(self, other):
		# overload the * operator for matrix multiplication
		return strassen_multiplication(self, other)

def create_submatrix(matrix,row_lower,row_upper,col_lower,col_upper):
	# create a submatrix from a larger one, given the bounds for row and column
	sub_mat = []
	for i in range(row_lower,row_upper):
		row = []
		for j in range(col_lower,col_upper):
			row.append(matrix.value[i][j])
		sub_mat.append(row)
	return Matrix(sub_mat)

def strassen_multiplication(P,Q):
	# Base case, return integer product
	if P.dim==1:
		return P.value[0][0] * Q.value[0][0]

	# Create submatrices
	A = create_submatrix(P, 0, P.dim/2, 0, P.dim/2)
	B = create_submatrix(P, 0, P.dim/2, P.dim/2, P.dim)
	C = create_submatrix(P, P.dim/2, P.dim, 0, P.dim/2)
	D = create_submatrix(P, P.dim/2, P.dim, P.dim/2, P.dim)

	E = create_submatrix(Q, 0, Q.dim/2, 0, Q.dim/2)
	F = create_submatrix(Q, 0, Q.dim/2, Q.dim/2, Q.dim)
	G = create_submatrix(Q, Q.dim/2, Q.dim, 0, Q.dim/2)
	H = create_submatrix(Q, Q.dim/2, Q.dim, Q.dim/2, Q.dim)

	# Perform recursive multiplications
	P_1 = A*(F-H)
	P_2 = (A+B)*H
	P_3 = (C+D)*E
	P_4 = D*(G-E)
	P_5 = (A+D)*(E+H)
	P_6 = (B-D)*(G+H)
	P_7 = (A-C)*(E+F)

	# Wrapping up, putting it all together
	# Final Terms 
	T_AE = P_5 + P_4 - P_2 + P_6
	T_BF = P_1 + P_2
	T_CG = P_3 + P_4
	T_DH = P_1 + P_5 - P_3 - P_7

	# Combine sub matrices to form elements of result matrix
	R = []
	for i in range(P.dim):
		R.append([])
		for j in range(Q.dim):
			if i<P.dim/2:
				if j<Q.dim/2:
					R[i].append(T_AE.value[i][j] if type(T_AE) is not int else T_AE)
				else:
					R[i].append(T_BF.value[i][j-Q.dim/2] if type(T_BF) is not int else T_BF)
			else:
				if j<Q.dim/2:
					R[i].append(T_CG.value[i-P.dim/2][j] if type(T_CG) is not int else T_CG)
				else:
					R[i].append(T_DH.value[i-P.dim/2][j-Q.dim/2] if type(T_DH) is not int else T_DH)
	return Matrix(R)

def main():
	infile = open("Matrix Input.txt","r")
	n = int(infile.readline())

	# Input P
	p = []
	for i in range(n):
		row = [int(num) for num in infile.readline().split(' ')]
		p.append(row)
	P = Matrix(p)
	print P

	print "multiplied by\n"

	# Input Q
	q = []
	for i in range(n):
		row = [int(num) for num in infile.readline().split(' ')]
		q.append(row)
	Q = Matrix(q)
	print Q

	print "equals\n"

	R = P * Q
	print R

if __name__ == "__main__":
	main()