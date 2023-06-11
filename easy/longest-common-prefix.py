# Title: Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""


def longestCommonPrefix(strs: list[str]):
    firstWord = strs[0]
    lastWord = strs[-1]
    prefix = ""
    for i in range(len(firstWord)):
        if (firstWord[i] == lastWord[i]):
            prefix += firstWord[i]
        else:
            break

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
