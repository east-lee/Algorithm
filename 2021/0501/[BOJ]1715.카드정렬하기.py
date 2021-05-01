def main():
  answer = 0
  N = int(input())
  deck = []
  for _ in range(N): deck.append(int(input()))

  while len(deck) != 1:
    deck.sort(reverse=True)
    A = deck.pop()
    B = deck.pop()
    answer += (A+B)
    deck.append(A+B)

  return answer

if __name__ == "__main__":
  print(main())