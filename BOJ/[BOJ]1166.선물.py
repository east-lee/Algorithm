def main():
  left,right = 0, max(L,W,H)

  for _ in range(10000):
    middle = (left+right)/2
    if (L//middle) * (W//middle) * (H//middle) >= N:
      left = middle
    else:
      right = middle
  print("%.10f"%(right))



if __name__ == "__main__":
  N, L, W, H = map(int,input().split())
  main()