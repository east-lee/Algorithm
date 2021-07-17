def check_prime(num):
  if num < 2: return False

  for i in range(2,int(num**0.5) + 1):
    if num % i == 0:
      return False

  return True

def make_prime(k=0, num=''):
  if k == N:
    print(num)
    return

  for i in range(10):
    new_num_str = num + str(i)
    new_num_int = int(new_num_str)
    if check_prime(new_num_int):
      make_prime(k+1,new_num_str)



if __name__ == "__main__":
  N = int(input())
  make_prime()