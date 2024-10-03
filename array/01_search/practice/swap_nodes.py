class Node:
    def __init__(self,val) -> None:
        self._val = val
        self.left = None
        self.right = None
        self.level = 0

    def __str__(self) -> str:
        return str(self._val)        
    
    


def swap_nodes(indexes,queries):
    root = Node(1)
    root.level = 1

    queue = [root]
    for left,right in indexes:
        node = queue.pop(0)
        if left != -1:
            node.left = Node(left)
            queue.append(node.left)
        if right != -1:
            node.right = Node(right)
            queue.append(node.right)


def inorder_swap(node,level,result):
    if node.level % level ==0:
        node.left, node.right = node.right, node.left
    
    if node.left != None:
        node.left.level = node.level+1
        inorder_swap(node.left)
    
    result.append(int(str(node)))

    if node.right != None:
        node.right.level = node.level+1
        inorder_swap(node.right)