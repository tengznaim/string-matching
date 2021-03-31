# String Matching Algorithms

This is a repository for string matching algorithms I wrote and played around with as additional exercise for WIA2005 - Algorithm Design and Analysis and part of our group Viva.

These algorithms were either written from understanding (and hence may have issues with different inputs or can be implemented in a more efficient manner) or based on provided pseudocodes during lectures.

## Algorithms Currently Implemented

- Naive Matching
  - Nested loops that theoretically has a time complexity of O(nm) (I think)
- Knuth Morris Pratt Algorithm (KMP)
  - Single function implementation of the GFG guide, can be split into two functions to handle creating the LPS array.
  - Time complexity is theoretically O(n+m), n being the length of the string and m being the length of the pattern.
- Trie
  - Uses a TrieNode approach that has a dictionary and an isWord boolean as attributes.
  - Using the dictionary enables a more dynamic approach rather than needing to initialise lists with fixed sizes for alphabetic indexing, eg. "a" at arr[0]
  - Currently does not have an option to print the trie since it _probably_ requires a breadth first approach of searching to go through each node.

## References

1. KMP

- GFG Guide - https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
- LPS Explanation - https://www.youtube.com/watch?v=tWDUjkMv6Lc
- Concept Explanation - https://www.youtube.com/watch?v=V5-7GzOfADQ
