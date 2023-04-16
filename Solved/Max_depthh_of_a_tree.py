from typing import Optional


class TreeNode:
    def __init__(self,value,left:None,right:None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return "TreeNode("+str(self.value)+")"
        


def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    else:
        left = self.maxDepth(root.left)+1
        right = self.maxDepth(root.right)+1
    max_depth = left if left>right else right
    return max_depth
    

