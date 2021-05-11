for _ in range(10):
    q = []
    n = int(input())
    for _ in range(n):
        input_data = input()
        play, num = 0,0
        if input_data[0]=='i':
            play = input_data[0]
            num =input_data[2:]
            q.append(num)
        elif input_data[0]=='c':
            print(len(q))
        else:
            if q:
                oo = q.pop(0)
                print(oo)
            else:
                print('empty')