def main():
  global alpha

  for an in alpha_num:
    for i in range(len(an)):
      alpha[an[i]] += 10**(len(an) - i - 1)

  alpha = sorted(alpha.items(), key = lambda x:-x[1])

  for i in range(9,-1,-1):
    if alpha[i][0] not in cant_zero:
      tmp = alpha[i]
      alpha.remove(tmp)
      alpha.append(tmp)
      break

  result = 0

  for i in range(10):
    result += alpha[i][1] * (9-i)

  print(result)


def find_cant_be_zero():
  cant_zero = []

  for an in alpha_num:
    cant_zero.append(an[0])

  return cant_zero


def get_data():
  N = int(input())
  alpha_num = [ list(input()) for _ in range(N)]

  return [N, alpha_num]


if __name__ == "__main__":
  N, alpha_num = get_data()
  cant_zero = find_cant_be_zero()
  alpha = {
    chr(i+ord("A")) : 0 for i in range(10)
  }

  main()