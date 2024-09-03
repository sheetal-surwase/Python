#bfs
visited=[]
queue=[]
def bfs(graph,start,goal):
    visited.append(start)
    queue.append(start)
    while queue:
        m=queue.pop[0]
        print(m)
        if m==goal:
            print("Node is found")
            break
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
bfs(visited,graph,'A','F')


