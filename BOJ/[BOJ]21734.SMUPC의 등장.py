def main():
  for data in input_data:
    count_str = str(ord(data))
    count = 0
    for i in count_str:
      count += int(i)
    print(data*count)

if __name__ == "__main__":
  input_data = input()
  main()