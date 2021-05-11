n = int(input())
q = []
for _ in range(n):
    input_str = input()
    if "push" in input_str:
        q.append(int(list(input_str.split())[1]))
    elif input_str == "pop":
        if q:
            print(q.pop(0))
        else:
            print("-1")
    elif input_str == "size":
        print(len(q))
    elif input_str == "empty":
        if q: print(0)
        else: print(1)
    elif input_str == "front":
        if not q: print("-1")
        else:
            print(q[0])
    else:
        if not q: print("-1")
        else:
            print(q[-1])