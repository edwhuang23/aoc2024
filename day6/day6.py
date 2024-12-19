import copy

def read_file(file_name):
  lines = []
  with open(file_name, 'r') as f:
    for line in f:
      lines.append(line.strip())
    f.close()
  return lines

def get_map():
  map = []

  for line in read_file('day6.txt'):
    line_list = []
    for character in line:
      line_list.append(character)
    map.append(line_list)
  
  return map

def find_starting_position(map):
  for rowIndex in range(len(map)):
    for columnIndex in range(len(map[rowIndex])):
      if map[rowIndex][columnIndex] == '^':
        return rowIndex, columnIndex
  return -1, -1

def validate_position(map, rowIndex, columnIndex):
  return rowIndex >= 0 and rowIndex < len(map) and columnIndex >= 0 and columnIndex < len(map[rowIndex])

def construct_unique_position_key(rowIndex, columnIndex):
  return str(rowIndex) + ',' + str(columnIndex)

def construct_unique_position_with_direction_key(rowIndex, columnIndex, direction):
  return construct_unique_position_key(rowIndex, columnIndex) + '(' + str(direction[0]) + ',' + str(direction[1]) + ')'

def shift_direction_right(current_direction):
  if current_direction == (-1, 0):
    return (0, 1)
  elif current_direction == (0, 1):
    return (1, 0)
  elif current_direction == (1, 0):
    return (0, -1)
  else:
    return (-1, 0)

# Returns set of unique positions and boolean for whether route is an infinite loop
def simulate_guard_route(map):
  # Saved as row,column format
  unique_positions = set()
  unique_positions_with_direction = set()
  current_direction = (-1, 0)
  currRowIndex, currColumnIndex = find_starting_position(map)

  while validate_position(map, currRowIndex, currColumnIndex):
    # Save position and direction
    position_key = construct_unique_position_key(currRowIndex, currColumnIndex)
    position_with_direction_key = construct_unique_position_with_direction_key(currRowIndex, currColumnIndex, current_direction)

    if position_key not in unique_positions:
      unique_positions.add(position_key)
    
    if position_with_direction_key in unique_positions_with_direction:
        return unique_positions, True
    unique_positions_with_direction.add(position_with_direction_key)

    # Try to go up. If obstacle, turn right
    if validate_position(map, currRowIndex + current_direction[0], currColumnIndex + current_direction[1]) and map[currRowIndex + current_direction[0]][currColumnIndex + current_direction[1]] == '#':
      current_direction = shift_direction_right(current_direction)
      continue
    
    currRowIndex += current_direction[0]
    currColumnIndex += current_direction[1]

  return unique_positions, False

def part_1():
  map = get_map()
  unique_positions, _ = simulate_guard_route(map)

  print('Unique Positions: ' + str(len(unique_positions)))

def part_2():
  map = get_map()
  number_of_infinite_loop_positions = 0

  for rowIndex in range(len(map)):
    for columnIndex in range(len(map[rowIndex])):
      if map[rowIndex][columnIndex] != '.':
        continue
      new_map = copy.deepcopy(map)
      new_map[rowIndex][columnIndex] = '#'
      _, is_infinite_loop = simulate_guard_route(new_map)
      if is_infinite_loop:
        number_of_infinite_loop_positions += 1

  print('Number of Positions for Infinite Loop: ' + str(number_of_infinite_loop_positions))

def main():
  part_1()
  part_2()

if __name__ == '__main__':
  main()