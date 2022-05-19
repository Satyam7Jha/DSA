# Created By Satyam Jha
import sys, collections


# Only for Sublime
sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")

# Using a Python dictionary to act as an adjacency list
graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}

visited = set()  # Set to keep track of visited nodes of graph.


def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
if __name__ == "__main__":

    print("Following is the Depth-First Search")
    for i in graph:
        dfs(visited, graph, i)
