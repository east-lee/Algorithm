def main():
  A_n = DNA.pop()
  while len(DNA):
    B = DNA.pop()
    A_index = DNA_index.index(A_n)
    B_index = DNA_index.index(B)
    A_n = DNA_arr[B_index][A_index]
  print(A_n)

if __name__ == "__main__":
  DNA_index = ['A','G','C','T']
  DNA_arr = [
    ['A','C','A','G'],
    ['C','G','T','A'],
    ['A','T','C','G'],
    ['G','A','G','T']
  ]
  N = int(input())
  DNA = list(input())
  main()