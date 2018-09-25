"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-22 1:35
Given the head of a graph, return a deep copy (clone) of the graph.
Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors.
There is an edge between the given node and each of the nodes in its neighbors.


OJ's undirected graph serialization (so you can understand error output):
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.


As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.


Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
Note: The information about the tree serialization is only meant
so that you can understand error output if you get a wrong answer.
You don't need to understand the serialization to solve the problem.
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        visited = {}

        def dfs(n, r):
            for e in n.neighbors:
                copy = UndirectedGraphNode(e.label)
                if e.label not in visited:
                    r.neighbors.append(copy)
                    visited[n.label] = copy
                    dfs(e, copy)
                else:
                    r.neighbors.append(visited[n.label])

        res = UndirectedGraphNode(node.label)
        visited[node.label] = res
        dfs(node, res)
        return res

        """
        visited = {}
        def cloneHelper(node):
            if node and node not in visited:
                newNode = UndirectedGraphNode(node.label)
                visited[newNode.label] = newNode
                newNode.neighbors = [visited.get(n.label) or cloneHelper(n) for n in node.neighbors]
                return newNode
        return cloneHelper(node)
        """


s = Solution()
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n3 = UndirectedGraphNode(3)
n4 = UndirectedGraphNode(4)
n5 = UndirectedGraphNode(5)
n6 = UndirectedGraphNode(6)

n7 = UndirectedGraphNode(7)
n8 = UndirectedGraphNode(8)
n9 = UndirectedGraphNode(9)
n10 = UndirectedGraphNode(10)

n1.neighbors = [n2, n3, n4]
n2.neighbors = [n7, n8, n9, n10]
n3.neighbors = [n5, n6]

n4.neighbors = [n4]
ret = s.cloneGraph(n1)
print(1)
