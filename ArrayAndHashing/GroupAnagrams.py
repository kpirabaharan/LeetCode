from typing import List


def groupAnagram(strs: List[str]) -> List[List[str]]:
    # Solution is m*n*log(n); m = # of words, n = sort
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


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(strs=strs))
