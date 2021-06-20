def find_croatia():
  global croatia_alpha

  range_num = 3 if len(croatia_alpha) >= 3 else len(croatia_alpha)

  for n in range(range_num,0,-1):
    check_alpha = ''.join(croatia_alpha[:n])

    if check_alpha in croatia_change:
      croatia_alpha = croatia_alpha[n:]
      return 1
    
  croatia_alpha = croatia_alpha[1:]
  return 1


def main():
  count = 0
  while croatia_alpha:
    count += find_croatia()

  return count


if __name__ == "__main__":
  croatia_change = [
    'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='
  ]
  croatia_alpha = list(input())

  print(main())