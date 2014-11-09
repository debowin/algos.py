# Karatsuba Multiplication
# An efficient integer multiplication algorithm based on the Divide and Conquer paradigm.
# (Done)Handle the case of huge disparity in size - Appending zeroes to the left of smaller number.
# TODO Write an automated test script which generates random numbers and cross checks result of multiplication.

def equalizeLength(num1,num2):
	# Make both numbers of the same length
	diff = len(num1) - len(num2)

	if(diff>0):
		smaller = num2
		larger = num1
	else:
		diff = -diff
		smaller = num1
		larger = num2

	smaller = '0'*diff + smaller
	return smaller,larger

def karatsuba(num1,num2):
	# import pdb
	# pdb.set_trace()
	# Base Case
	if int(num1)<10 or int(num2)<10:
		return int(num1)*int(num2)
	# Recursive Growth
	a = num1[:len(num1)/2]
	b = num1[len(num1)/2:]
	c = num2[:len(num2)/2]
	d = num2[len(num2)/2:]

	product_ac = karatsuba(a,c)
	product_bd = karatsuba(b,d)
	aplusb = str(int(a)+int(b))
	cplusd = str(int(c)+int(d))
	aplusb,cplusd = equalizeLength(aplusb,cplusd)
	product_other = karatsuba(aplusb,cplusd)

	result = product_ac * 10**(len(num1) + len(num1)%2) + (product_other - product_ac - product_bd) * 10**((len(num1) + len(num1)%2)/2) + product_bd 
	return result

def main():
	num1 = raw_input("Enter the first multiplicand: ")
	num2 = raw_input("Enter the second multiplicand: ")

	num1,num2 = equalizeLength(num1,num2)
	ans = karatsuba(num1, num2)
	print int(num1),'x',int(num2),'=',ans

if __name__ == "__main__":
	main()