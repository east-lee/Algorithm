# 28% 시간초과
# if __name__ == "__main__":
#   S, P = list(list(input()) for _ in range(2))
#   result = 0
#   for i in range(len(S)):
#     if S[i] == P[0] and S[i:i+len(P)] == P:
#       result = 1
#       break
#   print(result)

# 29% 시간초과
# if __name__ == "__main__":
#   S, P = list(list(input()) for _ in range(2))
#   result = 0
#   for i in range(len(S)):
#     if S[i] == P[0] and i-1+len(P) < len(S) and S[i-1+len(P)] == P[-1] and S[i:i+len(P)] == P:
#       result = 1
#       break
#   print(result)

# KMP 알고리즘 , 코드 => 블로그 참조
def getPI(pattern):
  global pi

  j = 0
  for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
      j = pi[j - 1]
    if P[i] == P[j]:
      j += 1
      pi[i] = j


def KMP():
  getPI()
  j = 0
  for i in range(len(S)):
    while j > 0 and S[i] != P[j]:
      j = pi[j - 1]
    if S[i] == P[j]:
      if j == len(P) - 1:
        return True
      j += 1

  return False

if __name__ == "__main__":
  S, P = list(list(input()) for _ in range(2))
  pi = [0 for _ in range(len(P))]

  result = KMP()

  print(1) if result else print(0)