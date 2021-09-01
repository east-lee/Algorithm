if __name__ == "__main__":
  S, T = [list(input()) for _ in range(2)]

  while len(S) < len(T):
    if T[-1] == 'A':
      T = T[:-1]
    else:
      T = T[:-1][::-1]

  print(1) if S == T else print(0)
