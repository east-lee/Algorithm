def main():
  cnt = 0
  while True:
    cnt += 1
    check_dict = {}
    breaker = False
    for student_num in students_num_list:
      num_string = ''.join(student_num[:cnt])

      if num_string in check_dict.keys():
        breaker = True
        break
      else: check_dict[num_string] = 1
    if not breaker:
      break
  return cnt

if __name__ == "__main__":
  N = int(input())
  students_num_list = []

  for _ in range(N):
    student_num = list(input())[::-1]
    students_num_list.append(student_num)
  print(main())

