def read_file(file_name):
  lines = []
  with open(file_name, 'r') as f:
    for line in f:
      lines.append(line.strip())
    f.close()
  return lines

def get_reports():
  reports = []

  for line in read_file('day2.txt'):
    reports.append(line.split())
  
  return reports

def produce_report_alternate_options(report, lastIndex): 
  report_remove_curr_index = report.copy()
  del report_remove_curr_index[lastIndex]
  report_remove_prev_index = report.copy()
  del report_remove_prev_index[lastIndex - 1]
  return report_remove_curr_index, report_remove_prev_index

def is_report_safe(report, damp_num):
  if damp_num < 0:
    return False
  
  isIncreasing = int(report[1]) > int(report[0])

  for levelIndex in range(1, len(report)):
    diff = int(report[levelIndex]) - int(report[levelIndex - 1])

    if ((isIncreasing and diff <= 0) or (not isIncreasing and diff >= 0)) or (abs(diff) < 1 or abs(diff) > 3):
      # if does not satisfy, choose either first or second number of the pair we are comparing to remove
      report_remove_curr_index, report_remove_prev_index = produce_report_alternate_options(report, levelIndex)
      return is_report_safe(report_remove_curr_index, damp_num - 1) or is_report_safe(report_remove_prev_index, damp_num - 1)
    
  return True

def part_1():
  num_safe_reports = 0

  for report in get_reports():
    if is_report_safe(report, 0):
      num_safe_reports += 1

  print('Number of Safe Reports: ' + str(num_safe_reports))

def part_2():
  num_safe_reports = 0

  for report in get_reports():
    report_remove_curr_index, report_remove_prev_index = produce_report_alternate_options(report, 1)
    if is_report_safe(report, 1) or is_report_safe(report_remove_curr_index, 0) or is_report_safe(report_remove_prev_index, 0):
      num_safe_reports += 1

  print('Number of Safe Reports With Dampener = 1: ' + str(num_safe_reports))


def main():
  part_1()
  part_2()

if __name__ == '__main__':
  main()