# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        '''
        思路：这个题如果没记错的话，是京东的面试题
        今天我就来系统的思考一下这个问题
        首先一个节点有两种选择，偷或者不偷
        如果偷的话，它的孩子节点不能偷

        有一种情况，就是该节点没有选择，该节点的子节点也没有选择
        其实以下这种情况是正确的，但是会超时，应该进行优化

        def dfs_rob(node,flag):
            if not node:
                return 0
            # 如果选择rob该节点
            if flag:
                return node.val + dfs_rob(node.left,False) + dfs_rob(node.right,False)
            else:
                # 如果没有选择该节点，孩子节点其实有两种情况，选择或者不选择
                return max(dfs_rob(node.left,True),dfs_rob(node.left,False)) + max(dfs_rob(node.right,True),dfs_rob(node.right,False))

        return max(dfs_rob(root,True),dfs_rob(root,False))
        '''

        def robber_helper(node):
            '''
            该函数返回两个值，分别表示不偷该节点的最大值，偷该节点的最大值
            '''
            if node is None:
                return 0, 0
            left_no, left_yes = robber_helper(node.left)
            right_no, right_yes = robber_helper(node.right)

            res_left_max = max(left_no, left_yes) + max(right_no, right_yes)
            res_right_max = node.val + left_no + right_no
            return res_left_max, res_right_max

        return max(robber_helper(root))


