import functools
import operator
def find_trees(forest, slope):
  '''Find the number of trees, given a traversal slope (row, col)

  forest: list of strings representing the forest
  slope: (row, col). row = # to go down, col = # to go right.

  '''
  rows = len(forest)
  row_len = len(forest[0])
  down = slope[0]
  right = slope[1]

  row = 0
  col = 0
  tree_count = 0

  while row < rows - 1:
    row += down
    col += right
    col = col % row_len

    if forest[row][col] == "#":
      tree_count += 1

  return(tree_count)

def part1(data):
  forest = data.splitlines()
  return find_trees(forest, (1, 3))

def part2(data):
  forest = data.splitlines()
  slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

  trees_found = [find_trees(forest, s) for s in slopes]

  return functools.reduce(operator.mul, trees_found)
