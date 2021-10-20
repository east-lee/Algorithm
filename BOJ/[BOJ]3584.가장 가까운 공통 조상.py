from collections import deque

def get_data():
    N = int(input())
    visited = [False] * (N+1)
    visited[0] = True
    parent = [0] * (N+1)
    child = [[] for _ in range(N+1)]
    depth = [0] * (N+1)
    ROOT_NODE = -1

    for _ in range(N-1):
        parent_node, child_node = map(int, input().split())
        visited[child_node] = True
        parent[child_node] = parent_node
        child[parent_node].append(child_node)

    for i in range(1,N+1):
        if visited[i] == False:
            ROOT_NODE = i
            break

    dq = deque()
    dq.append(ROOT_NODE)

    while dq:
        check_node = dq.popleft()

        for c_node in child[check_node]:
            depth[c_node] = depth[check_node] + 1
            dq.append(c_node)



    return [N, depth, parent]

if __name__ == "__main__":
    TC = int(input())

    for _ in range(TC):
        N, depth, parent = get_data()
        start_node_1, start_node_2 = map(int, input().split())

        depth_1, depth_2 = depth[start_node_1], depth[start_node_2]
        node_1, node_2 = start_node_1, start_node_2

        while True:
            if depth_1 > depth_2:
                depth_1 -= 1
                node_1 = parent[node_1]
            elif depth_1 < depth_2:
                depth_2 -= 1
                node_2 = parent[node_2]
            else:
                if node_1 == node_2:
                    print(node_1)
                    break
                else:
                    depth_1, depth_2 = depth_1 - 1, depth_2 - 1
                    node_1, node_2 = parent[node_1], parent[node_2]
