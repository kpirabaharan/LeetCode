from typing import List
from time import time


def groupAnagram1(strs: List[str]) -> List[List[str]]:
    # Solution is O(m*n*log(n)); m = # of words, n = sort
    # Map to store result key is sorted word, value is list of anagrams
    result = {}

    # Iterate
    for word in strs:
        # Sort the word alphabetically
        sortedWord = tuple("".join(sorted(word)))
        # Check if sorted word is a key in result and append
        if sortedWord in result.keys():
            result[sortedWord].append(word)
        else:
            result[sortedWord] = [word]

    # Return the list of values
    return result.values()


def groupAnagram2(strs: List[str]) -> List[List[str]]:
    # Solution is O(m*n); m = # of words, n = sort
    # Map to store result
    result = {}

    # ASCII Value of a (97 - 122 = a - z)
    startingASCII = 97

    # Iterate through every word in list
    for word in strs:

        # Make a list where every element how many times a letter of s appears
        # This count list will be the key of result
        count = 26 * [0]

        # Iterate through every char and add to count list
        for c in word:
            count[ord(c) - startingASCII] += 1

        """ Convert count (list) to a tuple to make hashable (since tuples are
        immutable and allow duplicate numbers ex. duplicate 0s/1s) """
        if tuple(count) in result.keys():
            result[tuple(count)].append(word)
        else:
            result[tuple(count)] = [word]

    return result.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Run 1, Faster for shorter words
start = time()
Answer1 = groupAnagram1(strs=strs)
end = time()
print(end - start, Answer1)

# Run 2
start = time()
Answer2 = groupAnagram2(strs=strs)
end = time()
print(end - start, Answer2)
