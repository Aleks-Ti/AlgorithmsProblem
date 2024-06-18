from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
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


def main(test_case: TreeNode, test_case1: TreeNode, test_case2: TreeNode, test_case3: TreeNode, test_case4: TreeNode):
    assert Solution().getMinimumDifference(test_case) == 1
    assert Solution().getMinimumDifference(test_case1) == 1
    assert Solution().getMinimumDifference(test_case2) == 1
    assert Solution().getMinimumDifference(test_case3) == 47
    assert Solution().getMinimumDifference(test_case4) == 9


if __name__ == '__main__':
    # test case 1 example for me
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    # test case 2 example for me
    root1 = TreeNode(1)
    root1.left = TreeNode(0)
    root1.right = TreeNode(48)
    root1.right.right = TreeNode(49)
    root1.right.left = TreeNode(12)
    # test case 3 example for me
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    root2.right.left = TreeNode(2)
    # test case 3 example for me
    root3 = TreeNode(543)
    root3.left = TreeNode(384)
    root3.left.right = TreeNode(445)
    root3.right = TreeNode(652)
    root3.right.right = TreeNode(699)
    # test case 4 example for me
    root4 = TreeNode(236)
    root4.left = TreeNode(104)
    root4.left.right = TreeNode(227)
    root4.right = TreeNode(701)
    root4.right.right = TreeNode(911)
    main(root, root1, root2, root3, root4)
