def main():
  start_share , end_share = start//x, end//x
  check_num = start_share * x + y
  result = 0
  if start<=check_num<=end:
    result += 1
  if check_num + x <= end or check_num - x >= start:
    result += 2
  if result == 1:
    return check_num
  else:
    return 'Unknown Number'

if __name__ == "__main__":
  start, end = map(int,input().split())
  if end < start:
    start,end = end,start
  x, y = map(int,input().split())
  print(main())