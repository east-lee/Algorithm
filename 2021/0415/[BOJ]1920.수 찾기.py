def solution(v,start,end):
  if start>end: return 0

  mid = (start+end)//2

  if v == A[mid]: return 1
  elif v < A[mid]: end = mid-1
  elif v > A[mid]: start = mid+1
  return solution(v,start,end)


if __name__ == "__main__":
  N = int(input())
  A = list(map(int,input().split()))
  M = int(input())
  B = list(map(int,input().split()))
  A.sort()

  for i in B:
    print(solution(i,0,N-1))



