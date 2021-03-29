def solution(card,k_check,total_cnt):
  if total_cnt == 2:
    if card == result_card:
      for k in k_check:
        print(k,end =' ')
      print()
    return

  for k in range(1,11):
    if 1<=k<N and 1<=2**k<N:
      deck = card[:]
      first_deck = deck[:N-2**k]
      second_deck = deck[N-2**k:]

      i = 2

      while i <= k+1:
        lower_deck = second_deck[:len(second_deck) - 2**(k-i+1)] #이게위에있는거 내려가야하는거
        upper_deck = second_deck[len(second_deck)-2**(k-i+1):] #이게뒤에있는거 올라가야하는거
        lower_deck.extend(first_deck)
        first_deck = lower_deck
        second_deck = upper_deck
        i+=1
      second_deck.extend(first_deck)
      solution(second_deck,k_check+str(k),total_cnt+1)

N = int(input())

result_card = list(map(int,input().split()))


card = [i for i in range(1,N+1)]

solution(card,"",0)

