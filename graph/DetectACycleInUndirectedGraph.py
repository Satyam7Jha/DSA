# Created By Satyam Jha
import sys, collections, pprint


# # Only for Sublime
sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")


graph = [[1], [0, 2], [1, 3, 4], [2, 4], [3, 2]]

visited = set()


def dfs(s, graph, p):

    visited.add(s)

    print(s, "node")

    for adj in graph[s]:

        if adj not in visited:

            dfs(adj, graph, p)
        elif adj == s:
            print("detect Cycle")


def detectCycle(graph):
    for i in range(5):

        if i not in visited:

            dfs(i, graph, -1)


print(detectCycle(graph))
