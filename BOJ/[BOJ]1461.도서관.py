

def main():
  max_distance_list = []
  count = 0
  max_distance = 0
  minus_check = True
  for book_position in book_position_list:
    if count == M:
      max_distance_list.append(max_distance)
      count = 0
      max_distance = 0
    if minus_check and book_position > 0:
      minus_check = False
      if max_distance:
        max_distance_list.append(max_distance)
        max_distance = 0
        count = 0
    max_distance = max(abs(book_position),max_distance)
    count += 1
  if max_distance: max_distance_list.append(max_distance)
  return max_distance_list



if __name__ == "__main__":
  N, M = map(int,input().split())
  book_position_list = list(map(int,input().split()))
  book_position_list.sort()
  distance_list = main()
  distance_list.sort()
  result = 0
  for i in range(len(distance_list)):
    if i == len(distance_list)-1:
      result += distance_list[i]
    else:
      result += 2*distance_list[i]
  print(result)
