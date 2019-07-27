# Python program for printing
# all numbers containing 1,2 and 3


def printNumbers(numbers):

    # convert all numbers
    # to strings
    numbers = map(str, numbers)
    result = []
    for num in numbers:

        # check if each number
        # in the list has 1,2 and 3
        if ('1' in num and
            '2' in num and
                '3' in num):
            result.append(num)

    # if there are no
    # valid numbers
    if not result:
        result = ['-1']

    return sorted(result)


# Driver Code
numbers = [123, 1232, 456,
           234, 32145]
result = printNumbers(numbers)
print ', '.join(num for num in result)
