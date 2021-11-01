def get_prime():
	max_num = 10001	
	prime_check = [False] * max_num
	
	for i in range(2, max_num):
		if prime_check[i] == False:
			x = i * 2
			while x < max_num:
				prime_check[x] = True
				x += i
	return prime_check
			
def solution(num):
	mid_num = num // 2
	for i in range(mid_num, num):
		num_a, num_b = num-i, i
		if not prime_check[num_a] and not prime_check[num_b]:
			return [num_a, num_b]
	
if __name__ == "__main__":
	N = int(input())
	prime_check = get_prime()
	
	for _ in range(N):
		check_num = int(input())
		num_a, num_b = solution(check_num)
		print(num_a, num_b)


        
