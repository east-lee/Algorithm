def DFS(k=1):
  global print_result

  if print_result: return
  if k == 6:
    # if not zero_check(): return
    print_result = True
    for line in result:
      print(''.join(line))
    return

  N,M,check_part = puzzle[str(k)]

  for i in range(L):
    for j in range(L):
      if i + N > L or j + M > L:
        continue
      else:
        breaker = False
        return_arr = []
        for n in range(N):
          for m in range(M):
            if check_part[n][m] == '#' and result[i+n][j+m] != '0':
              breaker =  True
              break
            elif check_part[n][m] == '#':
              result[i+n][j+m] = str(k)
              return_arr.append([i+n,j+m])
          if breaker:break
        if not breaker:
          DFS(k+1)
      for y,x in return_arr:
        result[y][x] = '0'

# def zero_check():
#   for i in range(L):
#     for j in range(L):
#       if result[i][j] == 0:
#         return False
#   return True


if __name__ == "__main__":
  L = int(input())
  puzzle = {}
  print_result = False
  result = list(['0']*L for _ in range(L))
  for i in range(1,6):
    N,M = map(int,input().split())
    part = list(list(input()) for _ in range(N))
    puzzle[str(i)] = [N,M,part]

  DFS()

  if not print_result:
    print('gg')



# TC
# 5
# 2 5
# #####
# #..##
# 2 2
# ##
# ##
# 2 5
# #..##
# ##...
# 1 3
# ###
# 1 5
# #####
#
# ----
#
# 11111
# 12211
# 32233
# 33444
# 55555
#
#
#
#
#
# ---
#
# 5
# 2 5
# #####
# #...#
# 2 2
# ##
# ##
# 2 5
# #..##
# ##...
# 1 3
# ###
# 1 5
# #####
#
#
# 6
# 2 6
# ######
# #..###
# 2 2
# ##
# ##
# 2 6
# #..###
# ##...#
# 1 3
# ###
# 2 6
# ######
# ######
#
#
# 5
# 2 5
# ...##
# ###..
# 1 3
# ###
# 3 4
# ..##
# #...
# #...
# 2 4
# #.##
# ...#
# 3 5
# ....#
# #.#.#
# #####