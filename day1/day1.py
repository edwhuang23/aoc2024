def read_file(file_name):
  lines = []
  with open(file_name, 'r') as f:
    for line in f:
      lines.append(line.strip())
    f.close()
  return lines

def create_lists():
  left_list = []
  right_list = []

  for line in read_file('day1.txt'):
    line_list = line.split()
    left_list.append(int(line_list[0]))
    right_list.append(int(line_list[1]))
  
  return left_list, right_list

def part_1():
  total_distance = 0
  left_list, right_list = create_lists()
  
  left_list.sort()
  right_list.sort()

  for index in range(len(left_list)):
    total_distance += abs(left_list[index] - right_list[index])

  print('Total Distance: ' + str(total_distance))

def part_2():
  similarity_score = 0
  left_list, right_list = create_lists()
  right_list_count_dict = {}

  for number in right_list:
    if number not in right_list_count_dict:
      right_list_count_dict[number] = 0
    right_list_count_dict[number] += 1
  
  for number in left_list:
    if number in right_list_count_dict:
      similarity_score += number * right_list_count_dict[number]

  print('Similarity Score: ' + str(similarity_score))

def main():
  part_1()
  part_2()

if __name__ == '__main__':
  main()