def main(): #L,P,V => 연속하는 p 일중 L일만 사용가능, 휴가기간은 총 v
  mod_day = V%P
  cnt = (V//P)*L
  if mod_day <=L:
    cnt += mod_day
  else:
    cnt += L
  print(f'Case {tc}: {cnt} ')

if __name__ == "__main__":
  tc = 0
  while True:
    tc += 1
    L,P,V = map(int,input().split())
    if L+P+V == 0:break
    main()