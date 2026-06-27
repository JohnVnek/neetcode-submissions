"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if (node != None):
            node_map = {}
            def dfs(curr: Optional['Node']):
                if (curr):
                    clone = Node(val=curr.val)
                    node_map[curr] = clone
                    for adj in curr.neighbors:
                        if (adj not in node_map):
                            dfs(adj)
                        clone.neighbors.append(node_map[adj])
            dfs(node)
            return node_map[node]
        return None