if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    data = list(map(int,input().split()))
    N = data[0]
    data = data[1:]
    total_avg = sum(data)/N
    cnt = 0
    for i in data:
      if i > total_avg:
        cnt += 1
    print(f'{format(round(cnt/N*100,3),".3f")}%')
