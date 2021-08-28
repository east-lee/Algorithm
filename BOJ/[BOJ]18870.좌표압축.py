def get_data():
  N = int(input())
  arr = list(map(int, input().split()))

  return [N, arr]


if __name__ == "__main__":
  N, arr = get_data()
  new_arr = sorted(list(set(arr)))

  check_dict = {str(new_arr[i]):i for i in range(len(new_arr))}

  for num in arr:
    print(check_dict[str(num)], end=" ")