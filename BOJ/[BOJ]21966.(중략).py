def CASE_2():
  case_2_check_s= S[12:N-12]

  for s in case_2_check_s:
    if s == '.':
      return False
  return True

def CASE_3():
  print_result = S[:9] + ['......'] + S[-10:]
  return print_result

if __name__ == "__main__":
  N = int(input())
  S = list(input())

  if N <= 25: print(''.join(S))
  else:
    if CASE_2():
      print_result = S[:11] + ['...'] + S[N-11:]
      print(''.join(print_result))
    else:
      print(''.join(CASE_3()))
