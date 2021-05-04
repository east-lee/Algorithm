from collections import defaultdict

def main():
  global words
  greedy_dict = dict()
  for word in words:
    word_len = len(word)
    for i in range(word_len):
      if word[i] not in greedy_dict.keys(): greedy_dict[word[i]] = 0
      greedy_dict[word[i]] += 10**(word_len - i -1)

  greedy_dict = sorted(greedy_dict.items(),key=lambda x:x[1], reverse=True)

  word_link_num_dict = defaultdict()
  cnt = 9
  for alpha in greedy_dict:
    word_link_num_dict[alpha[0]] = cnt
    cnt -= 1

  result = []

  for word in words:
    num = ''
    for alpha in word:
      num += str(word_link_num_dict[alpha])
    result.append(int(num))

  return sum(result)



if __name__ == "__main__":
  N = int(input())
  words = [input() for _ in range(N)]
  print(main())