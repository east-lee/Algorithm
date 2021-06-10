def main(l):
  total_cnt = 0
  total_ccnt = 0

  for tree in trees:
    mod_tree_l = tree % l
    cnt_tree = tree // l
    cnt = 0
    cut_cnt = 0


    cnt += cnt_tree
    if mod_tree_l == 0:
      cut_cnt += (cnt_tree-1)
    else: cut_cnt += cnt_tree

    if cnt*W*l - cut_cnt*C <0: continue
    total_cnt += cnt
    total_ccnt += cut_cnt

  return total_cnt*W*l - total_ccnt*C



if __name__ == "__main__":
  N, C, W = map(int,input().split())
  trees = list()
  result = 0

  for _ in range(N):
    trees.append(int(input()))


  for cutting_length in range(1,max(trees)+1):
    result = max(result,main(cutting_length))
  print(result)



# def cut_fn(tree,length):
#   tree_cnt = 0
#   cut_cnt = 0
#   if tree == length:
#     tree_cnt += 1
#   while tree > length:
#     tree -= length
#     tree_cnt += 1
#     cut_cnt += 1
#   return [tree_cnt,cut_cnt]
#
# def main(tree):
#   total_cnt = 0
#   cutting_cnt = 0
#
#   for selected_tree in trees:
#     if selected_tree < tree: continue
#     tree_cnt, cut_cnt = cut_fn(selected_tree,tree)
#     total_cnt += tree_cnt
#     cutting_cnt += cut_cnt
#
#   price = total_cnt * tree * W
#   minus_price = cutting_cnt * C
#
#   return price-minus_price
#
# if __name__ == "__main__":
#   N, C, W = map(int,input().split())
#   trees = list()
#   result = 0
#
#   for _ in range(N): trees.append(int(input()))
#   trees.sort()
#
#
#   for tree in trees:
#     result = max(result,main(tree))
#   print(result)