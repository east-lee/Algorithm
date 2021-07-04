# 메모리에러 발생
# 100000 * 100000 에서 에러 발생하는 듯
# 보드를 만들지 않고 열 체크로만 문제 풀이 진행
# python3 => 시간초과
# pypy3 => 60% fail?

def main():
  global visited
  result = -1


  if N <= 3:
    return result

  result = []

  for i in range(N):
    row_check = False
    for j in range(N):
      if visited[j] or i==j or j == N-1-i: continue
      visited[j] = 1
      result.append(j+1)
      row_check = True
      break
    if not row_check:
      return -1

  return result

if __name__ == "__main__":
  N = int(input())
  visited = [0] * N

  result = main()

  if result == -1: print(-1)
  else:
    for r in result: print(r)





