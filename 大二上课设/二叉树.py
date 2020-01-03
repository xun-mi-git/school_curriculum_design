#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  : 寻觅
# @File    : 二叉树.py
# @Time    : 2019/12/31 2:19
# @Software: PyCharm

"""
二叉树的操作程序
主要内容：
设计一个与二叉树基本操作相关的程序。程序的主要功能如下：
①以树状形式输出；
②以先序、中序、后序三种方式输出；
③统计输出二叉树的结点总数、叶子总数、树高。
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:

    def __init__(self, root=None):
        self.__root = root

    # 清空树
    def clear(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def add(self, elem):
        """创建一个新分支"""
        # 创建结点
        new = Node(elem)
        # 判断是否为空树
        if self.__root is None:
            self.__root = new
        else:
            # 用来存放(deposit)节点的数组
            deposit = [self.__root]
            # 利用队列的思维来遍历树
            while deposit:
                # 弹出对头元素进行判断
                head = deposit.pop(0)
                # 判断所在结点的右子结点是否为空，如果右子结点不为空则可以直接找下一组

                if head.left is None:
                    head.left = new
                    return
                elif head.right is None:
                    head.right = new
                    return
                # 如果本节点已满则开始找左子结点的
                else:
                    # 将本节点的左右子结点添加到队列中进行下一轮的寻找
                    deposit.append(head.left)
                    deposit.append(head.right)

    def wide(self):
        """广度优先遍历"""
        # 判断是否为空树，如果是空树则直接输出
        if self.__root is None:
            return '空树'
        else:
            # 用来存放(deposit)节点的数组
            deposit = [self.__root]
            # 存放遍历出来的树
            wide_data = []
            # 利用队列的思维来遍历树
            while deposit:
                # 输出头元素
                head = deposit.pop(0)
                wide_data.append(head.data)
                if head.left is not None:
                    deposit.append(head.left)
                if head.right is not None:
                    deposit.append(head.right)
            return wide_data

    def before(self, root):
        """
        :param root: 传入头结点
        :return: 先序遍历
        """
        # 判断是否为空树，如果是空树则直接输出
        if root is None:
            return
        else:
            print(root.data, end=' ')
            self.before(root.left)
            self.before(root.right)

    def middle(self, root):
        """
        :param root: 传入头结点
        :return: 中序遍历
        """
        # 判断是否为空树，如果是空树则直接输出
        if root is None:
            return
        else:
            self.middle(root.left)
            print(root.data, end=' ')
            self.middle(root.right)

    def behind(self, root):
        """
        :param root: 传入头结点
        :return: 后序遍历
        """
        # 判断是否为空树，如果是空树则直接输出
        if root is None:
            return
        else:
            self.behind(root.left)
            self.behind(root.right)
            print(root.data, end=' ')

    def leaf(self):
        """二叉树叶子节点数量"""
        # 判断是否为空树，如果是空树则直接输出
        if self.__root is None:
            return 0
        else:
            # 用来存放(deposit)节点的数组
            deposit = [self.__root]
            # 利用队列的思维来遍历树
            while deposit:
                # 输出头元素
                head = deposit.pop(0)
                if head.left is None or head.right is None:
                    deposit.append(head)
                    return len(deposit)
                    break
                if head.left is not None:
                    deposit.append(head.left)
                if head.right is not None:
                    deposit.append(head.right)

    def depth(self):
        """二叉树深度"""
        i = 0
        depth = self.__root
        while depth is not None:
            i += 1
            depth = depth.left
        return i


if __name__ == '__main__':
    # 实例化树
    tree = Tree()
    # 添加树的节点
    lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    for nd in lis:
        tree.add(nd)
    while Tree:
        print('\n------------------------------------')
        print("""选择操作（默认为一个字母a-o的15节点树）
        1.以树状形式输出
        2.深度遍历
        3.结点总数、叶子总数与树高
        4.自定义树
        """)
        n = input('输入序号')
        if n == '1':
            i, j = 0, 0
            while i < len(tree.wide()):
                i = 2 * i + 1
                print(tree.wide()[j:i])
                j = i
        if n == '2':
            print("""请选择遍历方式
            1.先序遍历
            2.中序遍历
            3.后序遍历
            """)
            x = input('请输入序号')
            if x == '1':
                tree.before(tree.root)
            elif x == '2':
                tree.middle(tree.root)
            elif x == '3':
                tree.behind(tree.root)
        if n == '3':
            print('此树的结点总数为%s.\n叶子总数为%s.\n树高为%s.' % (len(tree.wide()), tree.leaf(), tree.depth()))
        if n == '4':
            # 清空树
            tree.clear()
            print('请输入新的树')
            node = input('将结点以空格隔开')
            list_node = node.split(' ')
            for node in list_node:
                tree.add(node)
