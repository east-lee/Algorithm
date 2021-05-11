def main(result, k, p, m ,s, d):
    global max_result, min_result
    if k == len(nums):
        if result > max_result: max_result =result
        if result < min_result: min_result = result
        return

    if p:
        main(result+nums[k],k+1,p-1,m,s,d)
    if m:
        main(result-nums[k],k+1,p,m-1,s,d)
    if s:
        main(result*nums[k],k+1,p,m,s-1,d)
    if d:

        main(result//nums[k] if result>=0 else -(-result//nums[k]),k+1,p,m,s,d-1)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int,input().split()))
    operator = list(map(int,input().split()))
    min_result = 1000000000
    max_result = -1000000000
    main(nums[0],1,operator[0],operator[1],operator[2],operator[3])
    print(max_result)
    print(min_result)