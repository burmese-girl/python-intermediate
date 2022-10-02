# https://app.codesignal.com/arcade/python-arcade/meet-python/MEgcxkQyYqFDdySnH
# def solution(a):
#     n = len(a)
# 
#     for i in range(n):
#         j = 1
#         for j in range(n):
#             if arr[i] < arr[j]:
#                 a[i], a[j] = a[j], a[i]
# 
#     return a

class TreeNode:
    pass


class Solution(object):
    """ generated source for class Solution """
    first = TreeNode()
    second = TreeNode()
    pre = TreeNode()

    def recoverTree(self, root):
        """ generated source for method recoverTree """
        if root == None:
            return
        self.first = None
        self.second = None
        self.pre = None
        inorder(root)
        temp = self.first.val
        self.first.val = second.val
        self.second.val = temp

    def inorder(self, root):
        """ generated source for method inorder """
        if root == None:
            return
        self.inorder(root.left)
        if self.first == None and (self.pre == None or self.pre.val >= root.val):
            self.first = pre
        if self.first != None and self.pre.val >= root.val:
            self.second = root
        self.pre = root
        self.inorder(root.right)


arr = [2,5, 88,4, 1, 5,66]
res = solution(arr)
print(res)
