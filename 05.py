import bisect

def binaryseatsearch(seat_str, lo, hi, seat_range, lo_index, hi_index):
  '''Modified binary search to find either the column or row number

  seat_str: Each char indicates whether to select the upper or lower half. "FBFBFFB" for rows, or "RRL" for column

  lo: The char in seat_str that indicates selecting the lower half of the seat_range
  hi: The char in seat_str that indicates selecting the upper half of the seat_range
  seat_range: Number indicating the size of the seat range, like 128
  lo_index: Lower index of the seat_range
  hi_index: Higher index of the seat_range


  Returns: A column or row number
  '''

  if len(seat_str) == 1:
    if seat_str[0] == lo:
      return lo_index
    if seat_str[0] == hi:
      return hi_index
  else:
    if seat_str[0] == lo:
      seat_range = seat_range // 2
      hi_index = hi_index - seat_range
    if seat_str[0] == hi:
      seat_range = seat_range // 2
      lo_index = lo_index + seat_range
    return binaryseatsearch(seat_str[1:], lo, hi, seat_range, lo_index, hi_index)

def decode_boarding_pass(pass_str):
  '''Decodes a boarding pass to return a seat's row number, column number, and seat ID.

  pass_str: An encoded boarding pass represented as a string. Example: "FBFBFFBRRL"

  Returns: A decoded boarding pass - (seat_id, row, column)
  '''
  # First 7 chars finds the row
  row = binaryseatsearch(pass_str[0:7], "F", "B", 128, 0, 127)

  # Last 3 chars finds the column
  column = binaryseatsearch(pass_str[-3:], "L", "R", 8, 0, 7)

  seat_id = row * 8 + column
  return (seat_id, row, column)

def part1(data):
  all_passes = data.splitlines()

  highest_seat_id = 0

  for p in all_passes:
    seat_id = decode_boarding_pass(p)[0]
    if seat_id > highest_seat_id:
      highest_seat_id = seat_id
  
  return highest_seat_id


def part2(data):
  all_passes = data.splitlines()

  all_seat_ids = []

  for p in all_passes:
    seat_id = decode_boarding_pass(p)[0]
    bisect.insort(all_seat_ids, seat_id)

  t = 0
  for s in all_seat_ids:
    # Search for adjacent list items with a diff of 2
    if (all_seat_ids[t+1] - all_seat_ids[t]) == 2:
      # Your seat is between them
      return s+1
    t = t + 1
    
  
  