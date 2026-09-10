class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return 0, 0  # (sum, node_count)

            # Traversal: get sum and node count from left and right subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            # Calculate total sum and count for the current node's subtree
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            # Check if average (rounded down) equals current node's value
            if total_sum // total_count == node.val:
                self.count += 1

            return total_sum, total_count

        dfs(root)
        return self.count