def main():
  check_length = N
  while True:
    for i in range(N-check_length+1):
      check_arr = arr[i:i+check_length]
      print(check_arr,check_length)
      if max(check_arr) - min(check_arr) <= 2:
        return check_length
    check_length -= 1





if __name__ == "__main__":
  N = int(input())
  arr = list(map(int,input().split()))
  print(main())