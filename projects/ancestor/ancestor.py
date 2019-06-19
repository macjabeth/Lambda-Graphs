class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
  graph = dict()

  # loop over all tuples
  for t in ancestors:
    # check if tuple exists
    if t[1] not in graph:
      # create if not
      graph[t[1]] = set()
    # add edge
    graph[t[1]].add(t[0])

    # start depth-first search
    def dfs(starting_vertex):
      nonlocal graph
      if starting_vertex not in graph:
        return -1
      visited = set()
      s = Stack()
      distances = dict()
      s.push([starting_vertex])
      while s.size() > 0:
        path = s.pop()
        vtx = path[-1]
        if vtx not in visited:
          if vtx in graph:
            # we can traverse it
            for neighbor in graph[vtx]:
              path_new = path[:]
              path_new.append(neighbor)
              s.push(path_new)
              if neighbor not in graph:
                distances[neighbor] = len(path_new)
                continue
            visited.add(vtx)
      return min([k for k, v in distances.items() if v == max([v for k, v in distances.items()])])

    return dfs(starting_node)

# 1) find the furthest element that we can go to from the given node in a dgraph (dgraph = directed graph)
# 2) select the algorithm based on the problem - BFS if you want to find the shortest paths or DFS if you want to find the longest paths
# 3) think of what is an input and how to transform it // build a graph
# 4) think of the output and what we need to do to get it and structure it in an appropriate form // what if we do not have the result or cannot execute our function
# 5) start coding
