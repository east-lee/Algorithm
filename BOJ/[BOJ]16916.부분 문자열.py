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
  j = 0
  for i in range(1, len(pattern)):
    while j > 0 and pattern[i] != pattern[j]:
      j = pi[j - 1]
    if pattern[i] == pattern[j]:
      j += 1
      pi[i] = j


def KMP(s, pattern):
  getPI(pattern)
  j = 0
  for i in range(len(s)):
    while j > 0 and s[i] != pattern[j]:
      j = pi[j - 1]
    if s[i] == pattern[j]:
      if j == len(pattern) - 1:
        return True
      else:
        j += 1
  return False


s = input()
pattern = input()
pi = [0 for x in range(len(pattern))]

if KMP(s, pattern):
  print('1')
else:
  print('0')