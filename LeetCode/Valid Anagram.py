# Given two string s and t, write a function to determine if t is an anagram of s
# Anagram = a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
# Note: You may assume the string contains only lowercase alphabets.


def isAnagram(s, t):
    if set(s) == set(t):
        for char in list(set(s)):
            if s.count(char) != t.count(char):
                return False
        return True

    return False


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("cat", "car"))
    print(isAnagram("", ""))
    print(isAnagram("ab", "ba"))
    print(isAnagram("a", "ba"))
