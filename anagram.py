"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


def is_anagram(word1, word2):
    word1_map = {}  # letter: number of occurrences
    word2_map = {}  # letter: number of occurrences

    # return false if words are not the same length
    if len(word1) != len(word2):
        return False

    # building the hash maps
    for i in range(len(word1)):
        # we are counting the occurrences of each letter in word1
        word1_map[word1[i]] = 1 + word1_map.get(word1[i], 0)  # return zero if the value does does appear again
        word2_map[word2[i]] = 1 + word2_map.get(word2[i], 0)

    # iterating through the keys to see if the values (number of occurrences) of each char (letter) match
    for char in word1_map:
        print(str(word1_map[char]) + "--" + str(word2_map[char]))
        if word1_map[char] != word2_map.get(char, 0):
            return False  # return false if there is no match

    return True


s = "anagram"
t = "nagaram"

s2 = "rat"
t2 = "car"

s3 = 'banana'
t3 = 'nnabam'

print(is_anagram(s3, t3))
