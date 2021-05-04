if __name__ == "__main__":
    A,B,V = map(int,input().split())
    one_day = A-B
    result = (V-B) / (one_day)
    if result != int(result):
        result = int(result)+1
    print(int(result))