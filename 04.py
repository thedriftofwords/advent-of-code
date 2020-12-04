import functools

valid_years = {
  "eyr": {"min": 2020, "max": 2030},
  "iyr": {"min": 2010, "max": 2020},
  "byr": {"min": 1920, "max": 2002}
}
valid_pid_len = 9
valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def is_eye_color_valid(eye_color):
  return eye_color in valid_eye_colors

def is_pid_valid(pid):
  return len(pid) == valid_pid_len

def are_all_years_valid(passport):
  "Checks validity of birth, issue and expiration years"
  year_keys = valid_years.keys()
  for key in year_keys:
    passport[key] = int(passport[key])
    if not (valid_years[key]["min"] <= passport[key] <= valid_years[key]["max"]):
      return False
  return True

def is_hair_color_valid(hair_color):
  # Leading character must be '#'
  if hair_color[0] != '#':
    return False
  
  if len(hair_color) != 7:
    return False

  # After leading #, chars must be numeric or a-f
  for c in hair_color[1:7]:
    if not (c.isnumeric() or ("a" <= c <= "f")):
      return False
  
  return True

def is_height_valid(height):

  # Make sure last 2 chars are alphanumeric
  if not height[-2:].isalpha():
    return False
  else:
    measurement = int(height[:-2])
  
  units = height[-2:]

  if units == "cm":
    return 150 <= measurement <= 193
  if units == "in":
    return 59 <= measurement <= 76
  else:
    return False
     
def parse_passport(passport_list):
  "Converts each passport list of strings to a dict"

  passport = {}
  for field in passport_list:
    passport.__setitem__(field[0:3], field[4:])

  return passport
  
def auto_validate(passport):
  "Tests each passport-dict against the stricter auto-validation criteria, and returns True if everything passes"

  checks = []

  checks.append(is_hair_color_valid(passport["hcl"]))
  checks.append(are_all_years_valid(passport))
  checks.append(is_eye_color_valid(passport["ecl"]))
  checks.append(is_pid_valid(passport["pid"]))
  checks.append(is_height_valid(passport["hgt"]))

  return functools.reduce(lambda x, y: x and y, checks)

def prevalidate(passport):
  '''Prevalidates a passport for Part 1 criteria.
  '''
  # contains all fields
  if len(passport) == 8:
    return True
  # missing one field
  if len(passport) == 7:
    s = "".join(passport)
    # If missing the "cid" field, it's valid.
    return s.find("cid") == -1

  return False

def read_prevalidate_count(data):
  '''Divides batch into passports, and prevalidates each passport after it is batched. 
  
  Returns the number of prevalidated passports.
  '''
  
  # to capture the last passport in the batch
  data.append('')

  num_valid = 0
  data_len = len(data)
  passport = ""

  for r in range(data_len):
    passport += data[r]
    
    if data[r] == '':
      p = passport.split()
      if prevalidate(p):
        num_valid += 1
      passport = ""
    else:
      passport += " "
  
  return num_valid

def read_validate_count(data):
  '''Divides batch into passports. Prevalidates each one after it is batched, and then autovalidates the prevalidated passports. 
  
  data: list of strings
  Returns the number of autovalidated passports.
  '''
  
  # to capture the last passport in the batch
  data.append('')

  num_valid = 0
  data_len = len(data)
  passport = ""

  for r in range(data_len):
    passport += data[r]
    
    if data[r] == '':
      p = passport.split()
      if prevalidate(p):
        p = parse_passport(p)
        if auto_validate(p):
          num_valid += 1
      passport = ""
    else:
      passport += " "
  
  return num_valid

def part1(data):
  lines = data.splitlines()
  return read_prevalidate_count(lines)

def part2(data):
  lines = data.splitlines()
  return read_validate_count(lines)