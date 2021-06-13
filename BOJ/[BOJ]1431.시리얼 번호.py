def serial_sum(serial):
  return_sum = 0

  for num in serial:
    try:
      num = int(num)
      return_sum += num
    except: continue
  return return_sum


def check(i,j):
  A, B = serial_numbers[i], serial_numbers[j]

  if len(A) != len(B):
    if len(A) < len(B): return i
    else: return j
  else:
    sum_A, sum_B = serial_sum(A), serial_sum(B)
    if sum_A < sum_B: return i
    elif sum_B < sum_A: return j
    else:
      check_list = [(A,i),(B,j)]
      check_list.sort(key=lambda x:x[0])
      return check_list[0][1]





if __name__ == "__main__":
  N = int(input())
  serial_numbers = []

  for _ in range(N): serial_numbers.append(input())

  for i in range(N-1):
    min_idx = i
    for j in range(i,N):
      min_idx = check(min_idx,j)
    serial_numbers[i], serial_numbers[min_idx] = serial_numbers[min_idx], serial_numbers[i]

  for serial_number in serial_numbers:
    print(serial_number)