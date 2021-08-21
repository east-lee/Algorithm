def make_segmant_tree(index, start, end):
  global segmant_tree

  if start == end:
    num = arr[start]
    segmant_tree[index] = num
    return num
  mid = (start + end) // 2
  segmant_tree[index] = make_segmant_tree(2*index, start, mid) + make_segmant_tree(2*index + 1, mid + 1, end)
  return segmant_tree[index]


def get_sub_sum(index, start, end, left, right):
  if start > right or left > end:
    return 0

  if left <= start and end <= right:
    return segmant_tree[index]
  mid = (start+end)//2
  return get_sub_sum(index*2, start, mid, left, right) + get_sub_sum(index*2+1, mid+1, end, left, right)


def update_tree(index, start, end, changed_index, diff):
  global segmant_tree

  if changed_index < start or  changed_index > end:
    return

  segmant_tree[index] += diff

  if start != end:
    mid = (start+end)//2
    update_tree(index * 2, start, mid, changed_index, diff)
    update_tree(index * 2 + 1, mid+1, end, changed_index, diff)

if __name__ == "__main__":
  # N 원소의 개수 / M 변경 횟수 / K 구간의 합 출력 개수
  N, M, K = map(int, input().split())
  arr = list(int(input()) for _ in range(N))
  segmant_tree = [0] * (N * 4)

  make_segmant_tree(1, 0, N-1)

  for _ in range(M+K):
    command, a, b = map(int, input().split())

    if command == 1:
      diff = b - arr[a - 1]
      arr[a - 1] = b
      update_tree(1, 0, N - 1, a - 1, diff)

    else:
      print(get_sub_sum(1,0,N-1,a-1,b-1))
