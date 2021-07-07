def calculate_link_cnt(arr1,arr2):
  result = -1

  for i in range(len(arr1)):
    for j in range(len(arr2)):
      if arr1[i] == arr2[j]:
        result = i+j
        return result
  return result


def get_parent_list(person_num):
  parent_list = [person_num]
  x = person_num

  while parent[x] != x:
    parent_list.append(parent[x])
    x = parent[x]

  return parent_list


def get_data():
  N = int(input())
  searching_1, searching_2 = map(int, input().split())
  parent = [i for i in range(N+1)]
  m = int(input())

  for _ in range(m):
    parent_num, child_num = map(int, input().split())
    parent[child_num] = parent_num

  return [searching_1, searching_2, parent]



if __name__ == "__main__":
  S1, S2, parent = get_data()

  S1_parent_list, S2_parent_list = get_parent_list(S1), get_parent_list(S2)
  result = calculate_link_cnt(S1_parent_list,S2_parent_list)

  print(result)