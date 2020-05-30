import sys
import math


def get_closest_two_exits_node(init, graph, nodes_to_skip, goals):

    queue = [init]
    mem = set(queue)

    while len(queue) > 0:
        current = queue.pop(0)
        if current in goals:
            return current
        elif current in nodes_to_skip:
            for neighbour in [n for n in graph[current] if n not in mem]:
                queue.insert(0, neighbour)
        else:
            for neighbour in [n for n in graph[current] if n not in mem]:
                queue.append(neighbour)
        mem.add(neighbour)
    print('BFS failed.', file=sys.stderr)

def clean_data(dic, n1, n2):
    return {
    k: [v for v in nodes if ((k != n1) | (v != n2))]
    for k,nodes in dic.items() if ((k != n1) | (nodes != [n2]))  
}

def transfert_two_to_one_exit(one_exits, two_exits):
    element_to_transfert = [
        (node, exits) for node, exits in two_exits.items() if len(exits)==1]
    if len(element_to_transfert)>0:
        node_transfered, exit_transfered = element_to_transfert[0]
        one_exits[node_transfered] = [exit_transfered[0]]
        del two_exits[node_transfered]
    return one_exits, two_exits

nbr_nodes, nbr_links, nbr_exits = [int(i) for i in input().split()]

graph = {}
for n in range(nbr_nodes):
    graph[n] = []

for _ in range(nbr_links):
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].append(n2)
    graph[n2].append(n1)

exits = set([int(input()) for _ in range(nbr_exits)])

nodes_to_exits = {
    node: list(set(nodes) & exits)
        for node, nodes in graph.items() if len(list(set(nodes) & exits)) > 0}

two_exits = {k:v for k,v in nodes_to_exits.items() if len(v) == 2}
one_exits = {k:v for k,v in nodes_to_exits.items() if len(v) == 1}

# game loop
while True:

    skynet = int(input())
    n1, n2 = -1,-1

    if skynet in nodes_to_exits:
        n1 = skynet
        n2 = nodes_to_exits[skynet][0]

    elif len(two_exits) > 0:
        n1 = get_closest_two_exits_node(skynet, graph,
                list(one_exits.keys()), list(two_exits.keys()))
        n2 = two_exits[n1][0] 

    else:
        n1 = list(one_exits.keys())[0]
        n2 = one_exits[n1][0]

    nodes_to_exits = clean_data(nodes_to_exits, n1, n2)
    one_exits = clean_data(one_exits, n1, n2)
    two_exits = clean_data(two_exits, n1, n2)
    one_exits, two_exits = transfert_two_to_one_exit(
        one_exits, two_exits)

    print(f"{n1} {n2}")
