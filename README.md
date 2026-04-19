Word Search Solver
A Python CLI tool that solves word search puzzles — finds words horizontally and vertically (both directions), highlights matches in uppercase, and reports which words were found. Diagonals are... a work in progress. 

# Features

Horizontal search — left→right and right→left
Vertical search — top→bottom and bottom→top
Highlights found words in-place (uppercase)
Reports found words and whether all words were located
Diagonal search (not yet implemented)


# Usage
bashpython main.py
The program reads from stdin in the following format:
Input Format
<X> <Y>
<word1> <word2> ... <wordN>
<row_1>
<row_2>
...
<row_Y>
ParameterDescriptionXGrid width (number of columns)YGrid height (number of rows)word1..NSpace-separated list of words to findrow_iEach row of the word search grid (space-free, one character per cell)
Example
Input:
5 4
CAT DOG
c a t x d
o x x x o
g x x x g
x x x x x
Output:
Found words: CAT DOG, these are all
C A T x D
o x x x O
g x x x G
x x x x x

If not all words are found, the suffix changes to rest are not there.


# How It Works
The solver runs in O(W × X × Y) time, where:

W = number of words to search
X × Y = grid dimensions

For each word, it checks:

Horizontal — every row slice of length len(word) is compared to both word and word[::-1]
Vertical — every column slice of length len(word) is compared to both word and word[::-1]

Found characters are uppercased in-place on the grid, so overlapping words are highlighted correctly.

# Limitations

No diagonal support yet (see TODO in source)
Overlapping word detection may double-uppercase cells (cosmetically harmless)
Input is not validated — malformed input will raise a runtime error
