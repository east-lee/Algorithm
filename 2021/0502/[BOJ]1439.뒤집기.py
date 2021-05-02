if __name__ == "__main__":
  input_string = input()
  cnt = 0
  for i in range(len(input_string)-1):
    if input_string[i] != input_string[i+1]:
      cnt += 1
  print( (cnt+1) // 2)