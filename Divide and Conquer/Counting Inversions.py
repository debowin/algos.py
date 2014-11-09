# Counting the number of inversions in a given array of integers.
# An inversion is an instance of i,j where i<j but A[i]>A[j] for the array A

counter = 0

def count_inversions(list_num):
	global counter
	if(len(list_num)==1):
		return [list_num[0]]

	first_half = list_num[:len(list_num)/2]
	second_half = list_num[len(list_num)/2:]
	first_half = count_inversions(first_half)
	second_half = count_inversions(second_half)

	i,j= 0,0
	result = []
	while i<len(first_half) and j<len(second_half):
		if(first_half[i]<second_half[j]):
			result.append(first_half[i])
			i+=1
		else:
			result.append(second_half[j])
			j+=1
			counter+=len(first_half)-i
	while i<len(first_half):
		result.append(first_half[i])
		i+=1
	while j<len(second_half):
		result.append(second_half[j])
		j+=1

	return result

def main():
	count = 0
	num_list = raw_input("Enter a space separated list of numbers: ")
	num_list = map(int,num_list.split())
	# print num_list
	print count_inversions(num_list)
	print "Count of Inversions =",counter
if __name__ == "__main__":
	main()