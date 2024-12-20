# Needleman-Wunsch and Smith-Waterman Algorithm using Python

The Needleman-Wunsch and Smith-Waterman algorithms are two fundamental techniques in bioinformatics for sequence alignment. The Needleman-Wunsch algorithm is used for global alignment, while the Smith-Waterman algorithm is designed for local alignment. This document provides Python implementations of both algorithms, along with explanations of their functionality.



## Explaination


The provided code implements both the Needleman-Wunsch and Smith-Waterman algorithms for sequence alignment in Python.

Needleman-Wunsch Algorithm

Initialization: A score matrix is created, initialized with gap penalties for the first row and column.

Matrix Filling: The matrix is filled based on match, delete, and insert scores. The maximum score for each cell is calculated.

Traceback: Starting from the bottom-right of the matrix, the optimal alignment is constructed by tracing back through the matrix based on the scores.

Smith-Waterman Algorithm

Initialization: Similar to Needleman-Wunsch, but the score matrix is initialized to zero.
