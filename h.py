#h) Dijkstra’s Algorithm


graph = {'a':{'b':11,'c':4},'b':{'c':2,'d':5},'c':{'b':3,'d':7,'e':3},'d':{'e':8},'e':{'d':7}}

def dijkstra_algo(graph, start, target):
    shortest_distance = {}
    predecessor_node = {}
    unseen_nodes = graph
    infinity = 99999
    path = []

    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    print(shortest_distance)

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node , weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor_node[child_node] = min_node
        unseen_nodes.pop(min_node)
    print(shortest_distance)
dijkstra_algo(graph, 'a', 'e')