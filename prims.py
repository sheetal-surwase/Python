import heapq

def prims(graph,start):
    visited=set()
    min_span_tree=[]
    heap=[(0,start)]
    while heap:
        weight,node=heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            min_span_tree.append((weight,node))
            for neighbour,neighbour_weight in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(heap,(neighbour_weight,neighbour))
    return min_span_tree

graph={
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 6)],
    'D': [('B', 5), ('C', 6)]
}
start_vertex='A'

min_span_tree=prims(graph,start_vertex)
for edge in min_span_tree:
    print(edge)