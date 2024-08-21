# A binary tree is a tree which is characterized by one of the following properties:

# It can be empty (null).
# It contains a root node only.
# It contains a root node with a left subtree, a right subtree, or both. These subtrees are also binary trees.
# In-order traversal is performed as

# Traverse the left subtree.
# Visit root.
# Traverse the right subtree.


#                                 Depth
#     1               1            [1]
#    / \             / \
#   2   3     ->    3   2          [2]
#    \   \           \   \
#     4   5           5   4        [3]
# In-order traversal of left tree is 2 4 1 3 5 and of right tree is 3 5 1 2 4.

# indexes [[2, 3], [-1, -1], [-1, -1]]
# queries [1, 1]
# create tree, create node , tree inorder 

#INSIGHTS -> YOU HAVE TWO METHODS TO TRAVERSE A TREE. BF AND DF
#INSIGHTS -> BF USES A QUEUE. YOU ADD THE ROOT AND DEQUEUE (POP(0)) TO GET THE LAST VALUE ADDED TO ADD THE NEXT CHILD.
#         -> [1],[(2,3)],[(4,5),(6,7)] THEN ADD ONE TO QUEUE, POP IT AND ADD 2 AND THREE AS LEFT AND RIGHT BUT ADD THEM INTO THE QUEUE. ETC...
#INSIGHTS -> in order traversal in DF depth first. You recursively go until you reach the end of the left node, then print it and do the right



class Node:
    def __init__(self,val) -> None:
        self._val = val
        self.left = None
        self.right = None

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

    
    results = []
    for level in queries:
        result = []
        inorder_swap(root,level,result)
        results.append(result)

    return results
    
    

def inorder_swap(node,level,result):
    if node.level % level ==0:
        temp = node.right
        node.right = node.left
        node.left = temp

    

    if node.left != None:
        node.left.level = node.level+1
        inorder_swap(node.left,level,result)

    result.append(int(str(node)))

    if node.right != None:
        node.right.level = node.level+1
        inorder_swap(node.right,level,result)

    
