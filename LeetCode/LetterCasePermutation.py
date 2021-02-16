# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. You can return the output in any order.


class Solution:
    def letterCasePermutation(self, S: str) -> list[str]:
        my_list = list(Solution.recursive_alg(self, S))

        return my_list

    def recursive_alg(self, s: str) -> str:
        if not s:
            yield ""

        else:
            first_letter = s[:1]
            if first_letter.lower() == first_letter.upper():
                for i in Solution.recursive_alg(self, s[1:]):
                    yield first_letter + i
            else:
                for i in Solution.recursive_alg(self, s[1:]):
                    yield first_letter.lower() + i
                    yield first_letter.upper() + i


if __name__ == "__main__":
    obj = Solution()
    print(obj.letterCasePermutation("a1b2"))
    print(obj.letterCasePermutation("3z4"))
    print(obj.letterCasePermutation("12345"))
    print(obj.letterCasePermutation("0"))
