def parseline(line):
  '''Parses a line for lower/upper bounds, the letter, and the password.

  Args:
  line: a str read from input.txt, such as "1-8 n: dpwpmhknmnlglhjtrbpx"

  Returns:
  (lower, upper, char): represents a password policy
  lower: Int. Lower bound
  upper: Int. Upper bound
  char: Str. The letter to look for
  password: Str. The password to validate
  '''
  parts = line.split(" ")
  bounds = parts[0].split("-")

  lower = int(bounds[0])
  upper = int(bounds[1])
  char = parts[1][0]
  password = parts[2]
  
  return (lower, upper, char), password
      
def validate_part1(policy, password):
  '''Validates a password, given a password
  policy

  Args:
  password: str, like 'dpwpmhknmnlglhjtrbpx'
  policy: tuple with the lower and upper bounds, and a character to check the password for - like (1, 8, 'n')
  '''
  count = 0
  
  lo = policy[0]
  hi = policy[1]
  char = policy[2]

  for c in password:
    if c == char:
      count += 1
    if count > hi:
      return False
  
  if count < lo:
    return False
  else:
    return True

def validate_part2(policy, password):
  '''Validates a password, given a password
  policy

  Args:
  password: str, like 'dpwpmhknmnlglhjtrbpx'
  policy: tuple with two character positions, 1-indexed - and a character to check the password for - like (1, 8, 'n')
  '''

  first = policy[0] - 1
  second = policy[1] - 1
  char = policy[2]

  return (password[first] == char) ^ (password[second] == char)

def part1(data):
  lines = data.splitlines()
  
  validated_count = 0

  for line in lines:
    policy, password = parseline(line)
    if validate_part1(policy, password):
      validated_count += 1
  
  return validated_count

def part2(data):
  lines = data.splitlines()
  
  validated_count = 0

  for line in lines:
    policy, password = parseline(line)
    if validate_part2(policy, password):
      validated_count += 1
  
  return validated_count
  