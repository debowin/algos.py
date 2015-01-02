"""
Counting the number of inversions in a given array of integers.
An inversion is an instance of i,j where i<j but A[i]>A[j] for the array A.
"""

COUNTER = 0


def count_inversions(list_num):
    """
    Here we basically piggyback on the merge sort technique.
    Given two sorted lists, while merging them,
    If element at index i, say Ian in left list is greater than element at index j, say John of right list,
    it means Ian and the elements that come after it in first list(which are greater than Ian) are also greater than John,
    but occur before it in the list.
    Hence, the number of inversions increases by len(left_list)-i
    """
    global COUNTER
    if len(list_num) == 1:
        return [list_num[0]]

    first_half = list_num[:len(list_num) / 2]
    second_half = list_num[len(list_num) / 2:]
    first_half = count_inversions(first_half)
    second_half = count_inversions(second_half)

    i, j = 0, 0
    result = []
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            j += 1
            COUNTER += len(first_half) - i
    while i < len(first_half):
        result.append(first_half[i])
        i += 1
    while j < len(second_half):
        result.append(second_half[j])
        j += 1

    return result


def main():
    """
    main function
    """
    num_list = raw_input("Enter a space separated list of numbers: ")
    num_list = map(int, num_list.split())
    # print num_list
    print count_inversions(num_list)
    print "Count of Inversions =", COUNTER
if __name__ == "__main__":
    main()
