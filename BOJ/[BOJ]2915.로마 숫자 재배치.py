def main(string):
  global min_num, result_roam_num

  if string in pos_num_list:
    num_10 = pos_num_list.index(string)
    if num_10 < min_num:
      result_roam_num = string
      min_num = num_10

def DFS_find_second_num(k=0,result='',index_list=[]):
  if k == len(first_num):
    main(result)
    return

  for i in range(len(first_num)):
    if i not in index_list:
      DFS_find_second_num(k+1,result+first_num[i],index_list+[i])

def find_pos_num():
  global pos_num_list

  for i in range(10):
    for j in range(10):
      pos_num_list.append(roam_num_2[i] + roma_num_1[j])

if __name__ == "__main__":
  roma_num_1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
  roam_num_2 = ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
  pos_num_list = []
  result_roam_num = ''
  min_num = 100

  find_pos_num()

  first_num = list(input())
  DFS_find_second_num()

  print(result_roam_num)