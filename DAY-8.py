class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Insert a value into the BST
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Find a node by value
def find_node(root, val):
    if root is None or root.val == val:
        return root
    elif val < root.val:
        return find_node(root.left, val)
    else:
        return find_node(root.right, val)

# Find the Lowest Common Ancestor in BST
def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

# -------------------------
# Example usage:

# Build BST from list
values = [6, 2, 8, 0, 4, 7, 9, 3, 5]
root = None
for val in values:
    root = insert(root, val)

# Define nodes
p = find_node(root, 2)
q = find_node(root, 8)

# Find LCA
lca = lowestCommonAncestor(root, p, q)
print("Lowest Common Ancestor:", lca.val)
