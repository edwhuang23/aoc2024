import re

def read_file(file_name):
  lines = []
  with open(file_name, 'r') as f:
    for line in f:
      lines.append(line.strip())
    f.close()
  return lines

def get_corrupted_memory():
  memory = []

  for line in read_file('day3.txt'):
    memory.append(line)
  
  return memory

def parse_mult_string(text):
  return int(text[4 : text.find(",")]) * int(text[text.find(",") + 1 : text.find("\)")])

def part_1():
  sum = 0
  corrupted_memory = get_corrupted_memory()

  for line in corrupted_memory:
    matches = re.findall("mul\(\d+,\d+\)", line)
    for match in matches:
      sum += parse_mult_string(match)

  print('Sum: ' + str(sum))

def part_2():
  sum = 0
  corrupted_memory = get_corrupted_memory()
  multiply_enabled = True

  for line in corrupted_memory:
    matches = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", line)
    for match in matches:
      if match == "do()":
        multiply_enabled = True
        continue
      elif match == "don't()":
        multiply_enabled = False
        continue
      
      if multiply_enabled:
        sum += parse_mult_string(match)

  print('Sum: ' + str(sum))


def main():
  part_1()
  part_2()

if __name__ == '__main__':
  main()