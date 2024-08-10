# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_diff = float('inf')
        self.prev = None

        def calculate_difference(node: TreeNode):
            if not node:
                return

            calculate_difference(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev.val))
            self.prev = node

            calculate_difference(node.right)

        calculate_difference(root)
        return self.min_diff


def main():
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    tree1 = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
    assert Solution().getMinimumDifference(tree) == 1
    assert Solution().getMinimumDifference(tree1) == 1


if __name__ == '__main__':
    main()
