class Passport:

  def __init__(self, birth_year, issue_year, expiration_year, height, hair_color, eye_color, passport_id, country_id=None):
    self.birth_year = birth_year
    self.issue_year = issue_year
    self.expiration_year = expiration_year
    self.height = height
    self.hair_color = hair_color
    self.eye_color = eye_color
    self.passport_id = passport_id
    self.country_id = country_id

  valid_years = {
    "eyr": {"min": 2020, "max": 2030},
    "iyr": {"min": 2010, "max": 2020},
    "byr": {"min": 1920, "max": 2002}
  }
  valid_pid_len = 9
  valid_eye_colors = {"amb", "blu", "brn",                        "gry", "grn", "hzl", "oth"}

  def is_eye_color_valid(eye_color):
    return eye_color in Passport.valid_eye_colors

  def is_pid_valid(pid):
    return len(pid) == Passport.valid_pid_len

  def are_all_years_valid(passport):
    "Checks validity of birth, issue and expiration years"
    year_keys = Passport.valid_years.keys()
    for key in year_keys:
      passport[key] = int(passport[key])
      if not (Passport.valid_years[key]["min"] <= passport[key] <= Passport.valid_years[key]["max"]):
        return False
    return True

  def is_hair_color_valid(hair_color):
    if len(hair_color) != 7:
      return False

    # Leading character must be '#'
    if hair_color[0] != '#':
      return False

    # After leading #, chars must be numeric or a-f
    for c in hair_color[1:7]:
      if not (("0" <= c <= "9") or ("a" <= c <= "f")):
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
    "Tests each passport-dict against the stricter auto-validation criteria"

    return Passport.is_hair_color_valid(passport["hcl"]) and Passport.are_all_years_valid(passport) and Passport.is_eye_color_valid(passport["ecl"]) and Passport.is_pid_valid(passport["pid"]) and  Passport.is_height_valid(passport["hgt"])

def pre_validate(passport_list):
  '''Filters passport list down to minimally valid passports
  per Part 1 criteria.

  Converts each prevalidated passport to a dict.
  '''
  valid_passports = []

  for p in passport_list:
    # contains 6 or fewer fields? not valid
    if len(p) <= 6:
      continue
    # contains all fields
    elif len(p) == 8:
      valid_passports.append(Passport.parse_passport(p))
    # missing one field
    elif len(p) == 7:
      s = "".join(p)
      # If missing the "cid" field, valid.
      if s.find("cid") == -1:
        valid_passports.append(Passport.parse_passport(p))
    else:
      continue

  return valid_passports


def get_passport_list(data):
  '''Converts passport list into a list of lists,
  one list per passport.
  '''
  
  # to capture the last passport in the batch
  data.append('')

  all_passports = []
  data_len = len(data)
  passport = ""

  for r in range(data_len):
    passport += data[r]
    
    if data[r] == '':
      all_passports.append(passport.split())
      passport = ""
    else:
      passport += " "
  
  return all_passports

def part1(data):
  lines = data.splitlines()
  passports = get_passport_list(lines)
  prevalidated = pre_validate(passports)
  return len(prevalidated)


def part2(data):
  lines = data.splitlines()
  passport_list = get_passport_list(lines)
  prevalidated = pre_validate(passport_list)

  auto_validated = [p for p in prevalidated if Passport.auto_validate(p)]

  return len(auto_validated)