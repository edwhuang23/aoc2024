from functools import cmp_to_key

def read_file(file_name):
  lines = []
  with open(file_name, 'r') as f:
    for line in f:
      lines.append(line.strip())
    f.close()
  return lines

def get_page_ordering_and_page_updates():
  page_ordering, page_updates = set(), []
  is_page_ordering = True

  for line in read_file('day5.txt'):
    if is_page_ordering:
      page_ordering.add(line)
    else:
      page_updates.append(line.split(','))

    if not line:
      is_page_ordering = False
  
  return page_ordering, page_updates

page_ordering, page_updates = get_page_ordering_and_page_updates()

def get_middle_page_number(page_list):
  return int(page_list[int(len(page_list) / 2)])

def verify_page_order(page_update):
  for index in range(len(page_update) - 1):
    key = page_update[index] + '|' + page_update[index + 1]
    if key not in page_ordering:
      return False
  return True

def page_order_compare(item1, item2):
  if (item1 + '|' + item2) in page_ordering:
    return -1
  elif (item2 + '|' + item1) in page_ordering:
    return 1
  else:
    return 0

def fix_page_order(page_update):
  return sorted(page_update, key=cmp_to_key(page_order_compare))

def part_1():
  sum = 0

  for page_update in page_updates:
    if verify_page_order(page_update):
      sum += get_middle_page_number(page_update)

  print('Sum: ' + str(sum))

def part_2():
  sum = 0

  for page_update in page_updates:
    if not verify_page_order(page_update):
      sum += get_middle_page_number(fix_page_order(page_update))

  print('Sum: ' + str(sum))

def main():
  part_1()
  part_2()

if __name__ == '__main__':
  main()