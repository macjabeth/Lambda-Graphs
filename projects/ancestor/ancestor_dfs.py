from collections import deque


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = dict()
    for tpl in ancestors:
        if tpl[1] not in graph:
            graph[tpl[1]] = set()
        graph[tpl[1]].add(tpl[0])

    def solve(starting_vertex):
        nonlocal graph
        if starting_vertex not in graph:
            return -1

        distances = dict()

        def dfs(starting_vertex):
            visited = set()
            stack = Stack()
            stack.push([starting_vertex])
            while stack.size() > 0:
                path = stack.pop()
                vertex = path[-1]  # last element in the array storing the path
                if vertex not in visited and vertex in graph:
                    for neighbor in graph[vertex]:
                        path_new = path[:]  # path.copy()
                        path_new.append(neighbor)
                        stack.push(path_new)
                        if neighbor not in graph:
                            callback(neighbor, path_new)
                            continue
                    visited.add(vertex)

        def callback(neighbor, path_new):
            distances[neighbor] = len(path_new)

        dfs(starting_vertex)
        return min([k for k, v in distances.items() if v == max([v for k, v in distances.items()])])
    return solve(starting_node)

# 1) find the furthest element that we can go to from the given node in a dgraph (dgraph = directed graph)
# 2) select the algorithm based on the problem - BFS if you want to find the shortest paths or DFS if you want to find the longest paths
# 3) think of what is an input and how to transform it // build a graph
# 4) think of the output and what we need to do to get it and structure it in an appropriate form // what if we do not have the result or cannot execute our function
# 5) start coding
