"""
A DNA strand is made up of four symbols: A, T, C, G. Each symbol has a complement:
A and T complement each other
C and G complement each other

Determine the reverse complement of a DNA string by reversing the symbols in the string and replacing each symbol in
the reversed string by its complement.

Example: GTCAG
Result: reverse the string GTCAG -> GACTG
        Replace each symbol by its complement GACTG -> CTGAC
        return CTGAC


create empty result string
for loop - for each letter in the reversed input string
    if letter equals A
        result string plus equal to T
    else if letter equals T
        result string plus equal to A
    else if letter equals C
        result string plus equal to G
    else
        result string plus equal to C

return result string

"""


def dna_complement(s):
    result_str = ''
    for letter in reversed(s):
        if letter == 'A':
            result_str += 'T'
        elif letter == 'T':
            result_str += 'A'
        elif letter == 'C':
            result_str += 'G'
        else:
            result_str += 'C'

    return result_str


if __name__ == "__main__":
    print(dna_complement("GTCAG"))
