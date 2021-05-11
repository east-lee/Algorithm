def main():
  trees = {}
  total_cnt = 0
  while True:
    tree = input()
    if not tree:break
    total_cnt += 1
    if tree in trees.keys(): trees[tree] += 1
    else: trees[tree] = 1
  trees_num = sorted(trees.items())

  return [trees_num, total_cnt]

if __name__ == "__main__":
  result,total_cnt = main()

  for name, num in result:
    print('{} {}'.format(name, round(num*100/total_cnt,4)))