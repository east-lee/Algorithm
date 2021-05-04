# 맨밑에서부터 시작해서 부모노드에게 현재 자신의 값을 전달해줌
# 만약 어떤 노드의 자식이 한개 이면 그노드가 끝이라고 가정하고 최댓값인지 판별
# 만약 자식이 두개 이상이라면 해당 노드가 원의 중심이라 생각하고 자식중 가장큰값 2개를 더한 값과 판별
# 또한 자식노드중 가장 큰값과 현재 노드가 부모노드로 가기 위한 값을 합처서 다음 노드로 값 전달
def main():
  result = 0
  for i in range(N,0,-1):
    # for k in tree: print(k)
    # print('--------------',i,result)
    if len(tree[i][1]) >= 2:
      mid_result = []
      max_value = 0
      for child in tree[i][1]:
        mid_result.append(tree[child][2])
        if tree[child][2] > max_value: max_value = tree[child][2]

      mid_result.sort()
      r = mid_result[-1] + mid_result[-2]
      if r > result:
        result = r
      tree[i][2] += max_value
      tree[tree[i][0]][1].append(i)
    elif len(tree[i][1]) == 1:
      tree[tree[i][0]][1].append(i)
      tree[i][2] += tree[tree[i][1][0]][2]
      result = max(result,tree[i][2])
    else:
      tree[tree[i][0]][1].append(i)
  return result

if __name__ == "__main__":
  N = int(input()) #node 개수
  tree=[[0,[],0] for _ in range(N+1)]
  # tree[0] -> 연결/ tree[1] --> 자식 수 / tree[2] ---> 현재노드가 다음노드로갈때 최대값
  for _ in range(N-1):
    s,e,v = map(int,input().split())
    tree[e][0] = s
    tree[e][2] = v

  result = main()
  print(result)


# 잘못생각함 중신이 꼭 첫번쨰 노드일 필요는없다/!!!!!!
# def main():
#   for _ in range(n-1):
#     s,e,v = map(int,input().split())
#     tree[s].append((e,v))
#
#   cnt = 0
#   result = 0
#   for child in tree[1]:
#     e,v = child
#     if not cnt: solution(e,v,'left')
#     else: solution(e,v,'right')
#     cnt += 1
#
#   if right_length: result += max(right_length)
#   result += max(left_length)
#   return result
#
# def solution(e,v,side):
#   global left_length, right_length
#   if not tree[e]:
#     print(v,side)
#     if side=='left': left_length.append(v)
#     else: right_length.append(v)
#     return
#   for child in tree[e]:
#     solution(child[0],v+child[1],side)
#
# if __name__ == "__main__":
#   n = int(input())
#   tree = [[] for _ in range(n + 1)]
#   left_length = []
#   right_length = []
#   print(main())
#   print(left_length,right_length)









