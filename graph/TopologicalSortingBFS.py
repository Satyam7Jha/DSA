# Created By Satyam Jha
import sys, collections


# # Only for Sublime
sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")

# TopologicalSort Only for Acyclic Graph


graph = [[2, 3], [3, 4], [3], [], []]
q = collections.deque()

degree = [0] * len(graph)

for i in sum(graph, []):

    degree[i] += 1


for i, j in enumerate(degree):
    if j == 0:
        q.append(i)


while q:

    curr = q.popleft()

    print(curr)

    for adj in graph[curr]:

        degree[adj] -= 1

        if degree[adj] == 0:
            q.append(adj)
