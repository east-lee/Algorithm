# def main(): runtime error
#   n = int(input())
#   number = []
#   for _ in range(n): number.append(input())
#   result = 'YES'
#   for i in number:
#     for j in number:
#       if i == j: continue
#       if len(j)>len(i) and j[:len(i)] == i:
#         result = 'NO'
#         break
#     if result == 'NO':break
#   return result

# def main(): RUNTIME ERROR (25%)
#   n = int(input())
#   numbers = [] #완성
#   mid_numbers=[] #완성직전단계들
#
#   for _ in range(n):
#     num = input()
#     if num in mid_numbers: return 'NO'
#
#     now_num = ''
#     for i in num:
#       now_num += i
#       if now_num in numbers: return 'NO'
#       mid_numbers.append(now_num)
#     numbers.append(num)
#   return 'YES'


def main():
  n = int(input())
  numbers_dict = {} #완성
  mid_numbers_dict = {} #중간완성

  for idx in range(n):
    num = input()
    if num in mid_numbers_dict.keys():
      wasting(n,idx)
      return 'NO'

    now_num = ''
    for i in num:
      now_num += i
      if now_num in numbers_dict.keys():
        wasting(n,idx)
        return 'NO'
      mid_numbers_dict[now_num] = 1

    numbers_dict[num] = 1
  return 'YES'

def wasting(n,idx):
  for _ in range(n-idx-1): input()



if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    print(main())