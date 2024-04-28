# Rotate 2D Matrix

This project focuses on implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise in Python. The solution involves transposing the matrix (swapping rows and columns) and reversing each row to achieve the rotation.

## Function Description

The `rotate_2d_matrix(matrix)` function takes an n x n 2D matrix as input and rotates it 90 degrees clockwise. It does not return anything but modifies the matrix in-place.

## Usage

To use the `rotate_2d_matrix` function, follow these steps:

1. Define your 2D matrix as a list of lists, where each inner list represents a row.
2. Call the `rotate_2d_matrix(matrix)` function with your matrix as the argument.

Example usage:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_2d_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Requirements

- Python 3.8.10 or higher
- Ubuntu 20.04 LTS or compatible environment
- All files should end with a new line
- The first line of all Python files should be `#!/usr/bin/python3`
- Use pycodestyle (version 2.8.0) for code style checks
- All modules and functions must be documented
- All files must be executable

## Notes

- The `rotate_2d_matrix` function modifies the matrix in-place, so there's no need to assign the result to a new variable.
- This project does not use any external modules or libraries, keeping the implementation focused on basic Python programming concepts.
