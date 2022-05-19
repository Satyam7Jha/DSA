# Created By Satyam Jha
import sys, collections


# # Only for Sublime
sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")


# Create a Stack and append a node after dfs


def dfs(adj, graph):
    #     print(adj)

    vis.add(adj)

    for i in graph[adj]:

        if i not in vis:
            dfs(i, graph)

    stack.append(adj)


graph = [[1], [3], [3, 4], [4], []]
stack = []
vis = set()

for i in range(len(graph)):

    if i not in vis:

        dfs(i, graph)

print(*stack[::-1])
