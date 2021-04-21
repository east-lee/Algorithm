from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    working = defaultdict(int)

    for _ in range(n):
        name, status = map(str,input().split())
        if status == 'enter':
            working[name] = 1
        else:
            working[name] = 0

    sorted_working_by_reverse_name = sorted(working.items(), key=lambda x:x[0], reverse=True)

    for name, status in sorted_working_by_reverse_name:
        if status: print(name)
