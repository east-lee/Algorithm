for _ in range(10):
    decoder = list(input())
    string = input()
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    result = ''
    for i in string:
        isupper = 0
        if i==' ':
            result += ' '
            continue
        if i.isupper():
            isupper = 1
        idx = alphabet.index(i.lower())
        if isupper:
            result += decoder[idx].upper()
        else:
            result += decoder[idx]
    print(result)