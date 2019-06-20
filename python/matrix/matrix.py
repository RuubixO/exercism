'''
Given a string representing a matrix of numbers, return the rows and columns of
that matrix.

So given a string with embedded newlines like:

```text
9 8 7
5 3 2
6 6 7
```

representing this matrix:

```text
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
```

your code should be able to spit out:

- A list of the rows, reading each row left-to-right while moving
  top-to-bottom across the rows,
- A list of the columns, reading each column top-to-bottom while moving
  from left-to-right.
'''


class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [[int(n) for n in row.split()]
                     for row in matrix_string.split('\n')]
        self.columns = [list(tup) for tup in zip(*self.rows)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
