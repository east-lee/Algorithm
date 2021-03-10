def main():
    global stack
    input_str = input()
    if "push" in input_str: stack.append(int(list(input_str.split())[1]))
    elif "pop" == input_str:
        if stack:
            print(stack.pop())
        else: print(-1)
    elif "size" == input_str: print(len(stack))
    elif "empty" == input_str:
        if stack: print(0)
        else: print(1)
    else:
        if stack: print(stack[-1])
        else: print(-1)

stack = []

if __name__=="__main__":
    n = int(input())
    for _ in range(n):
        main()
