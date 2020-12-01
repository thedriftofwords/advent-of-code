def get_ints(data):
  '''
  Returns a list of integers.
  data: string of numbers with \n delimiter, after reading in a textfile with a number on each line.
  '''
  strings = data.splitlines()
  ints = [int(s) for s in strings]
  return ints

def part1_naive(data):
  "Took 5ms 560µs"
    # data is automatically read from 01.txt

  ints = get_ints(data)
  ints_len = len(ints)

  i = 0
  j = 0

  for i in range(ints_len):
    for j in range(ints_len):
      if ints[i] + ints[j] == 2020:
        print(ints[i], ints[j])
        return ints[i] * ints[j]

  return "Error or no pair found"
  

def part1_opt(data):
  "Took 3ms 399µs"
  # data is automatically read from 01.txt
    
  ints = get_ints(data)
  ints_len = len(ints)

  i = 0
  j = 0
    
  for i in range(ints_len):
    diff = 2020 - ints[i]
    for j in range(ints_len):
      if ints[j] != diff:
        continue
      else:
        # print(ints[i], ints[j])
        return ints[i] * ints[j]

  return "Error or no pair found"

def part2_naive(data):
  "Took 204ms 589µs"

  ints = get_ints(data)
  ints_len = len(ints)

  i = 0
  j = 0
  k = 0

  for i in range(ints_len):
    for j in range(ints_len):
      for k in range(ints_len):
        if ints[i] + ints[j] > 2020:
          continue
        if ints[i] + ints[j] + ints[k] == 2020:
          # print(ints[i], ints[j], ints[k])
          return ints[i] * ints[j] * ints[k]

  return "Error or no set found"

def part2_opt(data):
  "Took 3ms 470µs"

  ints = get_ints(data)
  ints_len = len(ints)

  i = 0
  j = 0
  k = 0

  for i in range(ints_len):
    diff = 2020 - ints[i]
    for j in range(ints_len):
      if ints[j] >= diff:
        continue
      for k in range(ints_len):
        jk_sum = ints[j] + ints[k]
        if jk_sum != diff:
          continue
        else:
          # print(ints[i], ints[j], ints[k])
          return ints[i] * ints[j] * ints[k]

  return "Error or no set found"

def part1(data):
  # return part1_naive(data)
  return part1_opt(data)

def part2(data):
  # return part2_naive(data)
  return part2_opt(data)