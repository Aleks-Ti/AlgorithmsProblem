class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None = None) -> int:
        def inner_func(node: TreeNode, count: int = 0) -> int:
            left_count = 1 if node and node.left else 0
            right_count = 1 if node and node.right else 0
            if node is None:
                return count

            if not node.left and not node.right:
                return 1
            if node.left:
                left_count += inner_func(node.left, count)
            if node.right:
                right_count += inner_func(node.right, count)
            return max(left_count, right_count)

        if root is None:
            return 0
        else:
            return inner_func(root, 1)
        


def main():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    tree1 = TreeNode(1, None, TreeNode(2))
    assert Solution().maxDepth(tree) == 3
    assert Solution().maxDepth(tree1) == 2


if __name__ == '__main__':
    main()
