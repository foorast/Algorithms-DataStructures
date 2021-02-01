# In this programming assignment you will implement one or more of the integer multiplication algorithms described in
# lecture. To get the most out of this assignment, your program should restrict itself to multiplying only pairs of
# single-digit numbers.  You can implement the grade-school algorithm if you want, but to get the most out of the
# assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm. So: what's the
# product of the following two 64-digit numbers?
# 3141592653589793238462643383279502884197169399375105820974944592
# 2718281828459045235360287471352662497757247093699959574966967627


def karat(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m = max(len(str(x)), len(str(y)))
        m2 = m // 2

        a = x // 10 ** (m2)
        b = x % 10 ** (m2)
        c = y // 10 ** (m2)
        d = y % 10 ** (m2)

        z0 = karat(b, d)
        z1 = karat((a + b), (c + d))
        z2 = karat(a, c)

        return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** (m2)) + (z0)


def main():

    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    print("It should be: " + str(x * y))
    print("Mine was: " + str(karat(x, y)))


main()
