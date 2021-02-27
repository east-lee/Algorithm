for _ in range(10):
    n = int(input())
    nums = list(map(int,input().split()))
    m = int(input())
    first_result = 0
    second_result = 0
    for num in nums:
        if not m%num:
            first_result += num
        if num>=m and not num%m:
            second_result += num
    print(first_result)
    print(second_result)