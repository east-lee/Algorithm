def solution(arr):
  stack = []
  remove_idx = 0
  sum_val = 0
  total_cnt = 0
  for prime in arr:
    stack.append(prime)
    sum_val += prime

    while True:
      if sum_val > N:
        sum_val -= stack[remove_idx]
        remove_idx += 1
      elif sum_val == N:
        total_cnt += 1
        sum_val -= stack[remove_idx]
        remove_idx += 1
      else:
        break
  print(total_cnt)

def find_prime(n):
  prime_arr = [0]*(n+1)
  prime_arr[1] = 1
  return_arr = []
  for i in range(2,n+1):
    if prime_arr[i] == 1: continue
    else: return_arr.append(i)
    x = 2*i
    while x <=n:
      prime_arr[x] = 1
      x += i
  return return_arr

if __name__ == "__main__":
  N = int(input())
  prime = find_prime(N)

  solution(prime)