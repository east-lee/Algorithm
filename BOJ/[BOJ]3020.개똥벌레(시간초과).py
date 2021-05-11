def main():
  global broken_cnt

  for i in range(N):
    start, end = 1, H + 1
    check_num = int(input())
    if i % 2 == 0: #석순
      end = check_num + 1
    else: start =  H - check_num + 1
    for j in range(start,end): broken_cnt[j] += 1



if __name__ == "__main__":
  N, H = map(int,input().split())
  broken_cnt = [0]*(H+1)
  main()
  broken_cnt[0] = max(broken_cnt)
  min_value = min(broken_cnt)
  min_cnt = broken_cnt.count(min_value)
  print(min_value ,min_cnt)