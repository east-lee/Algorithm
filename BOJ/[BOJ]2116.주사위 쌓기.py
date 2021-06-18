import sys
sys.setrecursionlimit(100000)


def dfs(check_result, bottom_num, k):
  global max_result
  if k == N:
    if max_result < check_result: max_result = check_result
    return
  if (N-k)*6 + check_result < max_result: return
  dice = dice_list[k]
  bottom_index = dice.index(bottom_num)
  top_index = face_to_face[str(bottom_index)]

  next_result = check_result + find_max_side_num(dice,bottom_index,top_index)
  dfs(next_result,dice[top_index],k+1)



def find_max_side_num(arr,bottom_index, top_index):
  max_num = 0

  for i in range(6):
    if i == bottom_index or i == top_index: continue
    if arr[i] > max_num: max_num = arr[i]

  return max_num

if __name__ == "__main__":
  N = int(input())
  max_result = 0
  dice_list = [
    list(map(int,input().split())) for _ in range(N)
  ]

  face_to_face = {
    '0':5, '1':3, '2':4,
    '3':1, '4':2, '5':0
  }

  for i in range(6):
    bottom_index = i
    top_index = face_to_face[str(bottom_index)]
    dfs(find_max_side_num(dice_list[0],bottom_index,top_index),dice_list[0][top_index],1)

  print(max_result)