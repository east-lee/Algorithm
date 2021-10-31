def solution(num_a, num_b): 
    while num_b:        
        num_a = num_a%num_b
        num_a, num_b = num_b, num_a
    
    return num_a      
        
        

if __name__ == "__main__":
    N = int(input())
    
    for _ in range(N):
        A, B = map(int ,input().split())
        print(A*B // solution(A, B))
    
