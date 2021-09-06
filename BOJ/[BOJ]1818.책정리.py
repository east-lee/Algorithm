
def get_data():
  N = int(input())
  book_order = list(map(int ,input().split()))
  book_order = [0] + book_order

  # print(book_order)

  return [N, book_order]

if __name__ == "__main__":
  N, book_order = get_data()
  ordered_arr = [i for i in range(N+1)]
  arr = [
    [0] * (N+1) for _ in range(N+1)
  ]

  for i in range(1,N+1):
    for j in range(1,N+1):
       if book_order[i] == ordered_arr[j]:
         arr[i][j] = arr[i-1][j-1] + 1
       else:
         arr[i][j] = max(arr[i-1][j], arr[i][j-1])
  print(N-arr[-1][-1])
