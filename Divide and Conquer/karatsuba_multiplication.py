"""
Karatsuba Multiplication
An efficient integer multiplication algorithm based on the Divide and Conquer paradigm.
(Done)Handle the case of huge disparity in size - Appending zeroes to the left of smaller number.
TODO Write an automated test script which generates random numbers and cross checks result of multiplication.
"""


def equalize_length(num1, num2):
    """
    Make both numbers of the same length
    """
    diff = len(num1) - len(num2)

    if diff > 0:
        smaller = num2
        larger = num1
    else:
        diff = -diff
        smaller = num1
        larger = num2

    smaller = '0' * diff + smaller
    return smaller, larger


def karatsuba(num1, num2):
    """
    karatsuba integer multiplication function.
    """
    # Base Case
    if int(num1) < 10 or int(num2) < 10:
        return int(num1) * int(num2)
    # Recursive Growth
    part_a = num1[:len(num1) / 2]
    part_b = num1[len(num1) / 2:]
    part_c = num2[:len(num2) / 2]
    part_d = num2[len(num2) / 2:]

    product_ac = karatsuba(part_a, part_c)
    product_bd = karatsuba(part_b, part_d)
    aplusb = str(int(part_a) + int(part_b))
    cplusd = str(int(part_c) + int(part_d))
    aplusb, cplusd = equalize_length(aplusb, cplusd)
    product_other = karatsuba(aplusb, cplusd)

    result = product_ac * 10 ** (len(num1) + len(num1) % 2) + (product_other -
                                                               product_ac - product_bd) * 10 ** ((len(num1) + len(num1) % 2) / 2) + product_bd
    return result


def main():
    """
    main function
    """
    num1 = raw_input("Enter the first multiplicand: ")
    num2 = raw_input("Enter the second multiplicand: ")

    num1, num2 = equalize_length(num1, num2)
    ans = karatsuba(num1, num2)
    print int(num1), 'x', int(num2), '=', ans

if __name__ == "__main__":
    main()
