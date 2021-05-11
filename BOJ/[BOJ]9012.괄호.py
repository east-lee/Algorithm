def main():
    arr = input()
    stack = []
    result = "YES"
    for i in arr:
        if not stack and i=="(":
            stack.append(i)
        elif not stack:
            result = "NO"
            break
        elif i=="(":
            stack.append(i)
        elif i==")":
            stack.pop()
    if stack:
        result = "NO"
    return result


if __name__ == "__main__":
    T  = int(input())
    for _ in range(T):
        print(main())