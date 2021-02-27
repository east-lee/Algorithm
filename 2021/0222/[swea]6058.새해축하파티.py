T = int(input())

for t in range(1,T+1):
    B, L, N = map(int,input().split())
    all_wine = B * 750
    before_glass = 0

    checking = [0]*(400*401//2 + 1)
    layer_glass_num_check = [0]*401

    layer_cnt = 0
    while layer_cnt < L:
        layer_cnt += 1
        before_glass += layer_cnt
        layer_glass_num_check[layer_cnt] = before_glass

        if layer_cnt == L:
            cnt = 1
            layer = 1
            for i in range(1,layer_glass_num_check[L-1]+1):
                if cnt > layer_glass_num_check[layer]:
                    layer+=1
                checking[i] += 1
                checking[i+layer] += 1
                checking[i+layer+1]+=1
                cnt += 1

    used_wine = sum(layer_glass_num_check[:L]) * 250
    result = 0
    if B*750 <= used_wine:
        result = 0
    else:
        if L == 1:
            result = 250
        else:
            result = ((B*750 - used_wine) / (layer_glass_num_check[L]))*checking[N]
    if result >250:
        result =250
    print(layer_glass_num_check[:10],checking[:30],used_wine)
    print(f'#{t} {result}')





