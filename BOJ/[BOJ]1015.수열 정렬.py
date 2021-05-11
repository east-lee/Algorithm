
if __name__ == "__main__":
  N = int(input())
  A = list(map(int,input().split()))

  for i in range(N):
    A[i] = [A[i],i]
  B = A[:]
  B.sort(key=lambda x:(x[0],x[1]))

  for searching_list in A:
    print(B.index(searching_list),end=' ')