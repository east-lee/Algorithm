def main():
  global result, max_result

  cnt = 0

  while cnt < P:
    divid_num = 2

    while divid_num < 9:
      print(result,divid_num,cnt)
      result *= (divid_num+1 / divid_num )

      if result > max_num: break
      max_result = max(max_result, result)
      divid_num += 1

    cnt += 1


  return result


if __name__ == "__main__":
  D, P = map(int, input().split()) # D => 최대 D자리 이하, P번 곱하기
  max_num = int('9' * D)
  result = 2 ** P
  max_result = 0
  if max_num < result:
    print(-1)
  else:
    main()
    print(max_result)