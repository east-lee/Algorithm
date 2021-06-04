def main():
  global word_list
  word_list.sort(key=lambda x:(len(x),x))
  for word in word_list: print(word)

if __name__ == "__main__":
  N = int(input())
  word_list = []
  for _ in range(N):  word_list.append(input())
  word_list = list(set(word_list))
  main()