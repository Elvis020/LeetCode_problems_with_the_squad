class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def reverse_bin_tree(root: Node) -> Node:
    if not root:
        return

    # Swapping the left and right children
    root.left, root.right = root.right, root.left
    reverse_bin_tree(root.left)
    reverse_bin_tree(root.right)
    return root
