



if __name__ == "__main__":
  N, K = map(int,input().split())
  people = [i for i in range(1,N+1)]
  print_arr =[]
  idx = 0
  for i in range(N):
    idx += K-1
    if idx >= len(people):
      idx = idx % (len(people))
    print_arr.append(str(people.pop(idx)))

  print('<'+', '.join(print_arr)+'>')

