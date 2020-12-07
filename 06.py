def part1(data):
  lines = data.splitlines()
  lines.append('') # To capture last group
  count = 0
  
  answers = set()
  for line in lines:
    # End of current group
    if line == '':
      count += len(answers)
      answers = set()
    for l in line:
      answers.add(l)

  return count

def part2(data):
  lines = data.splitlines()
  lines.append('') # To capture the last group

  unanimous_count = 0
  group_count = 0

  answers = {}
  for line in lines:
    # End of current group
    if line == '':
      for k in answers.keys():
        if answers[k] == group_count:
          unanimous_count = unanimous_count + 1
      group_count = 0
      answers = {}
    else:
      group_count = group_count + 1
      for l in line:
        if l not in answers:
          answers[l] = 1
        else:
          answers[l] = answers[l] + 1

  return unanimous_count