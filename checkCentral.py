import time
import random




def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node

bigM = {}
AcList = []

def findSmallestCentral(G,actors):
    for actress in actors:
        bigM[actress],cen = dijkstra(G,actress)


def dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}

    for node in bigM.keys():
        if v in node:
            final_dist[node] = bigM[node][v]


    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
    
    central =  float(sum(final_dist)/len(final_dist))
    return final_dist, central



def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def top_k(L, k):
    v = L[random.randrange(len(L))]
    (left, middle, right) = partition(L, v)
    # middle used below (in place of [v]) for clarity
    if len(left) == k:   return left
    if len(left)+1 == k: return left + middle
    if len(left) > k:    return top_k(left, k)
    return left + middle + top_k(right, k - len(left) - len(middle))

def partition(L,v):
    smaller = []
    bigger = []
    for val in L:
        if val[0] < v[0]: smaller += [val]
        if val[0] > v[0]: bigger += [val]
    return (smaller, [v], bigger)


f = open('file.tsv','r')
G = {}
actors = set()

for line in f:
    (actor, movie,year) = line.split("\t")
    actors.add(actor)
    make_link(G,actor,movie)

d = []

for actress in actors:
    d +=[(centrality(G,actress),actress)]


c = top_k(d, 20)
c.sort(key=lambda x: x[0])
print c





