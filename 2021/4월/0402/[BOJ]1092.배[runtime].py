if __name__ == "__main__":
  N,crain = int(input()), list(map(int,input().split()))
  M,box = int(input()), list(map(int,input().split()))

  crain.sort(reverse=True)
  box.sort(reverse=True)
  moved = [0]*M

  if crain[0] < box[0]:
    print(-1)
  else:
    total_time = 0
    while 0 in moved:
      for i in range(N):
        for j in range(M):
          if not moved[j] and crain[i] >= box[j]:
            moved[j] = 1
            break
      total_time += 1
    print(total_time)