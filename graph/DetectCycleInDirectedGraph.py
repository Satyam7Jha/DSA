# Created By Satyam Jha
import sys, collections, pprint


# # Only for Sublime
sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")


graph = [[1], [], [1, 3], [4], [5], [3]]

vis = set()


def dfs(s, graph, prevNodes):
    print(prevNodes)

    vis.add(s)

    for i in graph[s]:

        if i in vis and i in prevNodes:

            print("cycle detect")

        elif i not in vis:
            dfs(i, graph, prevNodes + [i])


for i in range(6):

    if i not in vis:

        dfs(i, graph, [i])
