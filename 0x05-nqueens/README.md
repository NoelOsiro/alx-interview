Here's an example README.md file for your N Queens problem-solving program:

```markdown
# N Queens Solver

## Description
This program solves the N Queens problem, which involves placing N non-attacking queens on an N×N chessboard.

## Usage
```
Usage: nqueens N

If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
```

## Examples
```bash
./nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```bash
./nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Requirements
- Python 3
- PEP 8 style compliance

## Installation
No installation required. Just ensure Python 3 is installed on your system.

## Author
[Your Name]

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
```

Replace `[Your Name]` with your actual name or username. You can also include more sections or information as needed for your project.