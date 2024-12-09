def read_file(file_name):
  lines = []
  with open(file_name, 'r') as f:
    for line in f:
      lines.append(line.strip())
    f.close()
  return lines

def get_word_matrix():
  word_matrix = []

  for line in read_file('day4.txt'):
    word_matrix.append(line)
  
  return word_matrix

def check_word_with_direction(word_matrix, search_word, originRowIndex, originColumnIndex, rowDirection, columnDirection):
  currRowIndex, currColumnIndex = originRowIndex, originColumnIndex

  for letter in search_word:
    if currRowIndex < 0 or currRowIndex >= len(word_matrix):
      return False
    elif currColumnIndex < 0 or currColumnIndex >= len(word_matrix[currRowIndex]):
      return False

    if letter != word_matrix[currRowIndex][currColumnIndex]:
      return False
    
    currRowIndex += rowDirection
    currColumnIndex += columnDirection
  return True

def search_XMAS_from_spot(word_matrix, rowIndex, columnIndex):
  num_found = 0
  # At each letter, see if we can find XMAS
  # Once direction is established, only look in that direction

  # Up
  if check_word_with_direction(word_matrix, 'XMAS', rowIndex, columnIndex, -1, 0):
    num_found += 1

  # Right
  if check_word_with_direction(word_matrix, 'XMAS', rowIndex, columnIndex, 0, 1):
    num_found += 1

  # Left
  if check_word_with_direction(word_matrix, 'XMAS', rowIndex, columnIndex, 0, -1):
    num_found += 1

  # Down
  if check_word_with_direction(word_matrix, 'XMAS', rowIndex, columnIndex, 1, 0):
    num_found += 1

  # Upper Left Diagonal
  if check_word_with_direction(word_matrix, 'XMAS', rowIndex, columnIndex, -1, -1):
    num_found += 1

  # Upper Right Diagonal
  if check_word_with_direction(word_matrix, 'XMAS', rowIndex, columnIndex, -1, 1):
    num_found += 1
  
  # Lower Left Diagonal
  if check_word_with_direction(word_matrix, 'XMAS', rowIndex, columnIndex, 1, -1):
    num_found += 1
  
  # Lower  Right Diagonal
  if check_word_with_direction(word_matrix, 'XMAS', rowIndex, columnIndex, 1, 1):
    num_found += 1

  return num_found

def search_X_MAS_from_spot(word_matrix, rowIndex, columnIndex):
  first_diagonal_check, second_diagonal_check = False, False

  # Check first diagonal
  if (check_word_with_direction(word_matrix, 'AM', rowIndex, columnIndex, -1, -1) and check_word_with_direction(word_matrix, 'AS', rowIndex, columnIndex, 1, 1)) or (check_word_with_direction(word_matrix, 'AS', rowIndex, columnIndex, -1, -1) and check_word_with_direction(word_matrix, 'AM', rowIndex, columnIndex, 1, 1)):
    first_diagonal_check = True

  # Check second diagonal
  if (check_word_with_direction(word_matrix, 'AM', rowIndex, columnIndex, 1, -1) and check_word_with_direction(word_matrix, 'AS', rowIndex, columnIndex, -1, 1)) or (check_word_with_direction(word_matrix, 'AS', rowIndex, columnIndex, 1, -1) and check_word_with_direction(word_matrix, 'AM', rowIndex, columnIndex, -1, 1)):
    second_diagonal_check = True

  return first_diagonal_check and second_diagonal_check

def part_1():
  num_found = 0
  word_matrix = get_word_matrix()

  for rowIndex in range(len(word_matrix)):
    for columnIndex in range(len(word_matrix[rowIndex])):
      num_found += search_XMAS_from_spot(word_matrix, rowIndex, columnIndex)

  print('Found: ' + str(num_found))

def part_2():
  num_found = 0
  word_matrix = get_word_matrix()

  for rowIndex in range(len(word_matrix)):
    for columnIndex in range(len(word_matrix[rowIndex])):
      num_found += search_X_MAS_from_spot(word_matrix, rowIndex, columnIndex)

  print('Found: ' + str(num_found))


def main():
  part_1()
  part_2()

if __name__ == '__main__':
  main()