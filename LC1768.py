class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ms= ""
        val1 = len(word1)
        val2 = len(word2)
        if(val1>val2):
            j=0
            for i in range(val2):
                ms+=word1[i]+word2[i]
                j=i
            ms+=word1[j+1:]
        elif(val1<val2): 
            j=0
            for i in range(val1):
                ms+=word1[i]+word2[i]
                j=i
            ms+=word2[j+1:]            
        else:
            for i in range(len(word1)):
                ms+=word1[i]+word2[i]
    
        return ms


# 1768. Merge Strings Alternately
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 