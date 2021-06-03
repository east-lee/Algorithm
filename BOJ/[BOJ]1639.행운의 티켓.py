def main():
  N = len(ticket_number)
  check_length = N if N%2 == 0 else N-1
  result = 0
  while check_length > 0:
    for start_point in range(N):
      if start_point + check_length > N:
        break
      left_ticket, right_ticket = ticket_number[start_point:start_point+check_length//2], ticket_number[start_point+check_length//2:start_point+check_length]
      if sum(left_ticket) == sum(right_ticket):
        result = check_length
        break
    if result: break
    check_length -= 2
  print(result)

if __name__ == "__main__":
  ticket_number = list(map(int,list(input())))
  main()


