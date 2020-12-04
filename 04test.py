def validate_passports(passport_list):
  num_passports = len(passport_list)
  valid_passports = 0
  less_than_6 = 0
  all_fields = 0
  seven_fields = 0
  seven_missing_cid = 0
  other_cases = 0

  for p in passport_list:
    # contains 6 or fewer fields? not valid
    if len(p) <= 6:
      less_than_6 += 1
      #continue
    # contains all fields
    elif len(p) == 8:
      valid_passports += 1
      all_fields += 1
    # missing one field
    elif len(p) == 7:
      s = "".join(p)
      seven_fields += 1
      # If missing the "cid" field, valid.
      if s.find("cid") == -1:
        valid_passports += 1
        seven_fields += 1
        seven_missing_cid += 1
    else:
      # should be 0
      other_cases += 1
      continue
  
  print(f'num_passports: {num_passports}')
  print(f'valid_passports: {valid_passports}')
  print(f'less_than_6: {less_than_6}')
  print(f'all_fields: {all_fields}')
  print(f'seven_fields: {seven_fields}')
  print(f'seven_missing_cid: {seven_missing_cid}')
  print(f'other_cases: {other_cases}')
  return valid_passports

def test_each_validation(prevalidated):
  '''hcl: 191 // had a bug
  ecl: 193
  years: 178
  pid: 183 // had a bug
  hgt: 190 // had a bug
  '''

  hcl_valid = [p for p in prevalidated if Passport.is_hair_color_valid(p["hcl"])]

  print(len(hcl_valid))

  ecl_valid = [p for p in prevalidated if Passport.is_eye_color_valid(p["ecl"])]

  print(len(ecl_valid))

  years_valid = [p for p in prevalidated if Passport.are_all_years_valid(p)]

  print(len(years_valid))

  pid_valid = [p for p in prevalidated if Passport.is_pid_valid(p["pid"])]

  print(len(pid_valid))

  hgt_valid = [p for p in prevalidated if Passport.is_height_valid(p["hgt"])]

  print(len(hgt_valid))