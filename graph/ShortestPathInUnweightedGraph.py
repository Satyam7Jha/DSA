# Created By Satyam Jha
import sys, collections, pprint


# Only for Sublime
sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")


graph = {0: [0, 1, 2], 1: [0, 1, 2, 3], 2: [0, 1, 2, 3], 3: [1, 2, 3]}


s = 0

dis = [float("inf")] * len(graph)
dis[s] = 0

visited = {s}

q = collections.deque([s])

while q:

    curr = q.popleft()

    for adj in graph[curr]:

        if adj not in visited:

            dis[adj] = dis[curr] + 1

            visited.add(adj)
            q.append(adj)

print(dis)
