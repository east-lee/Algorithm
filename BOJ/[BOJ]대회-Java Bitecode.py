def main():
  JAVA = ['J','A','V']
  JAVA_Bitecode = ''
  for string in string_input:
    if string in JAVA:
      continue
    else:
      JAVA_Bitecode += string

  if len(JAVA_Bitecode) == 0:
    return 'nojava'
  return JAVA_Bitecode


if __name__ == "__main__":
  N = int(input())
  string_input = list(input())
  print(main())