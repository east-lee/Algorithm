if __name__ == "__main__":
  N = int(input())
  arr = []
  for _ in range(N): arr.append(int(input()))

  check = [0]*(max(arr)+1)

  for i in arr: check[i] += 1

  for i in range(N):
    result = -1
    check_point = 1
    while check_point ** 2 <= arr[i]:
      if arr[i] % check_point == 0:
        if check_point ** 2 == arr[i]:
          result += check[check_point]
        else: result += check[check_point] + check[arr[i]//check_point]
      check_point += 1
    print(result)
