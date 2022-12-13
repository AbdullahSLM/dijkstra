import sys
from heapq import heapify, heappush


def dijsktra(graph, src, dest):
    inf = sys.maxsize
    node_data = {}
    for key in graph:
        node_data[key] = {'cost': inf, 'pred': []}

    node_data[src]['cost'] = 0
    visited = []
    src_node = src
    for i in range(len(graph) - 1):
        if src_node not in visited:  
            min_heap = []
            for dest_node in graph[src_node]:
                if dest_node not in visited:
                    cost = node_data[src_node]['cost'] + graph[src_node][dest_node]
                    if cost < node_data[dest_node]['cost']:
                        node_data[dest_node]['cost'] = cost
                        node_data[dest_node]['pred'] = node_data[src_node]['pred'] + [src_node]
                    heappush(min_heap, (node_data[dest_node]['cost'], dest_node))
            visited.append(src_node)
        heapify(min_heap)
        
        src_node = min_heap[0][1]
        
    path = node_data[dest]['pred'] + list(dest)
    cost = node_data[dest]['cost']

    # print("Shortest Distance: " + str(cost))
    # print("Shortest Path: " + str(path))

    return (path, cost)


# if __name__ == "__main__":
#     inf = sys.maxsize
#     graph = {
#         'A': {'B': 2, 'C': 4, 'D': inf, 'E':inf, 'F': inf},
#         'B': {'A': 2, 'C': 3, 'D': 8, 'E':inf, 'F': inf},
#         'C': {'A': 4, 'B': 3, 'D': 2, 'E': 5, 'F': inf, },
#         'D': {'A': inf, 'B': 8, 'C': 2, 'E':11, 'F': 22},
#         'E': {'A': inf, 'B': inf, 'C': 5, 'D':11, 'F': 1},
#         'F': {'A': inf, 'B': inf, 'C': inf, 'D': 22, 'E': 1}
#     }

#     # graph = {
#     #     'A': {'B': 2, 'C': 4},
#     #     'B': {'A': 2, 'C': 3, 'D': 8},
#     #     'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
#     #     'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
#     #     'E': {'C': 5, 'D': 11, 'F': 1},
#     #     'F': {'D': 22, 'E': 1}
#     # }



#     # top = Tk()





#     # graph = {}
#     # n = int(input("Please enter the number of your nodes: "))

#     # for i in range(n):
#     #     node = str(input("Please enter node number : "))
#     #     list_of_nodes = {}
#     #     N = int(
#     #         input("Please enter the number of nodes associated with node:" + node))
#     #     for j in range(N):
#     #         associated_nodes = str(input("Please enter node number:"))
#     #         node_cost = int(input("Please enter the value of node " + associated_nodes))
#     #         list_of_nodes[associated_nodes] = node_cost
#     #     graph[node] = list_of_nodes

#     # source = str(input("Please enter the source node"))
#     # destination = str(input("Please enter the target node"))
#     # dijsktra(graph, source, destination, n)


#     source = 'A'
#     destination = 'F'
#     dijsktra(graph, source, destination)
#     # top.mainloop()
