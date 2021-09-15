def get_idx(word):
  idx = ord(word) - ord('A') if ord('A') <= ord(word) <= ord('Z') else ord(word) - ord('a') + 26
  return idx


def get_data():
  g, s = map(int, input().split())
  W, S = (list(input()) for _ in range(2))

  return [g, s, W, S]


if __name__ == "__main__":
  g, s, W, S = get_data()

  check = [0] * 52
  check_s = [0] * 52
  result = 0

  for word in W:
    idx = get_idx(word)
    check[idx] += 1

  start, length = 0, 0

  for i in range(s):
    word = S[i]
    idx = get_idx(word)
    check_s[idx] += 1

    length += 1

    if length == g:
      if check == check_s:
        result += 1
      word = S[start]
      idx = get_idx(word)
      check_s[idx] -= 1
      start, length = start + 1, length - 1
  print(result)

