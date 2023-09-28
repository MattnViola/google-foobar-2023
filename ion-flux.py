class Node:
    def __init__(self, parent):
        self.parent = parent

def solution(h, q):
    # I'm just going to reverse build it.
    nodes = {}
    val = [2**h - 1]
    def buildTree(height, parent):
        nodes[val[0]] = Node(parent)
        curr = val[0]
        val[0] -= 1
        if height == 1:
            return
        # right child
        buildTree(height - 1, curr)
        # left child
        buildTree(height - 1, curr)
        
    buildTree(h, -1)
    res = []
    for num in q:
        res.append(nodes[num].parent)
    return res

print(solution(5, [19, 14, 28]))