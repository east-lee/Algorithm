def main():
  first_right = (x2-x1)*(y2-y1)
  first_left = (f-x1)*(y2-y1)
  if f == 0: first_left=0
  first_cnt = first_right+first_left
  if not c:
    return first_cnt
  w_divid = H//(c)
  return first_cnt *w_divid

if __name__ == "__main__":
  W, H, f, c, x1, y1, x2, y2 = map(int,input().split())
  print(W*H-main())