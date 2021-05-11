#stack 풀이
# def main():
#   string = input()
#   bomb = input()
#   stack = ''
#   for i in string:
#     stack += i
#     if i == bomb[-1] and len(stack)>=len(bomb):
#       while stack and stack[-len(bomb):] == bomb:
#         stack = stack[:-len(bomb)]
#
#   if not stack: return 'FRULA'
#   return stack


def main():
  arr, check = list(list(input()) for _ in range(2))
  stack = []

  for i in arr:
    stack.append(i)
    if check[-1] == i and len(stack) >= len(check):
      while stack and stack[-len(check):] == check:
        for _ in range(len(check)):stack.pop()
  if not stack:return 'FRULA'
  return ''.join(stack)


if __name__ == "__main__":
  print(main())