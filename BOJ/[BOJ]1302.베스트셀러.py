if __name__ == "__main__":
  N = int(input())
  best_seller = {}

  for _ in range(N):
    book_title = input()
    if book_title in best_seller.keys():
      best_seller[book_title] += 1
    else:
      best_seller[book_title] = 1

  best_seller = sorted(best_seller.items(),key=lambda x:x[1],reverse=True)

  max_cnt = best_seller[0][1]
  title_list = []
  for title,cnt in best_seller:
    if max_cnt == cnt:
      title_list.append(title)
    else:
      break

  title_list.sort()

  print(title_list[0])