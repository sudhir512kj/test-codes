# Python3 program to merge n number of strings

# Function performing the calculations


def solve(a, b, k):
    s = ""

    # Length of string a
    la = len(a)

    # Length f string b
    lb = len(b)
    l = la + lb

    # Pointers for string
    # a and string b
    indexa = indexb = 0

    while l:
        # pa and pb denote the number
        # of characters of both
        # a and b extracted
        pa = pb = 0

        # If entire substring of length
        # k can be extracted
        if la - indexa >= k:
            s = s + a[indexa: indexa + k]
            indexa = indexa + k
            pa = k

        # If the remaining string is
        # of length less than k
        elif la - indexa < k and la - indexa:
            s = s + a[indexa: la]
            pa = la - indexa
            indexa = la

        # If the string has been
        # traversed
        elif indexa >= la:
            pa = 0

        # If entire substring of
        # length k can be extracted
        if lb - indexb >= k:
            s = s + b[indexb: indexb+k]
            pb = k
            indexb = indexb + k

        # If the remaining string is of
        # length less than k
        elif lb - indexb < k and lb - indexb:
            s = s + b[indexb: lb]
            pb = lb - indexb
            indexb = lb

        # If the string has been
        # traversed
        elif indexb >= lb:
            pb = 0
        l = l - pa - pb

    print(s)


# Driver function
a = "determination"
b = "stance"
k = 3
solve(a, b, k)
