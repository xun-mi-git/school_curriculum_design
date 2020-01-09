#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  : 寻觅
# @File    : 银行排队系统.py
# @Time    : 2019/12/30 18:19
# @Software: PyCharm

"""
银行排队系统
主要内容：
设某银行有n个窗口开展对外接待业务，从银行开门起不断有客户开展业务。客户人数众多时需要选择窗口排队，实现取票进队、排队等待、叫号服务。系统的主要功能如下：
①客户到达银行时能拿到排除号码，并能知道需要等待的人数。如果是VIP客户直接进入VIP窗口，无须加入普通客户的等待；
②可查看每个银行窗口正在给几号客户办理业务；
③客户离开银行时，有评价窗口银行职员服务的平台。
"""


# 假设有任意个常规窗口和1个VIP窗口
class Queue:
    # 队列取号查号呼叫操作
    def __init__(self):
        # 用队列的方式进行银行排队
        self.__window = []

    def queueing(self, num):
        """
        客户获得排队序号
        :param num:客户序号
        :return: 输出当前排队人数
        """
        # 在队列尾部添加最新排队的人
        self.__window.append(num)
        return self.__window

    # 当前队列的长度
    def __len__(self):
        return len(self.__window)

    # 输出对头
    def pop(self):
        return self.__window.pop(0)


class Eva:
    # 窗口评价
    def __init__(self):
        # 存储当前窗口和正在服务的客户,使用散列的结构进行存储。
        self.__items = {}
        # 使用双层散列的结构进行存储{窗口号：{客户号：评价内容, ……}, ……}
        self.__eva_items = {}

    def service(self, window_num, num):
        """
        存储正在服务的窗口
        :param window_num: 窗口
        :param num: 正在服务的用户号
        """
        self.__items[window_num] = num

    # 输出当前正在运行的窗口号
    @property
    def services(self):
        return self.__items

    def dete(self, window_num):
        """
        判定程序，判断此窗口之前是否有人存在，是否需要进行评价
        :param window_num: 窗口号
        :return: 是否需要评价
        """
        return self.__items.get(window_num, False)

    def eva_sys(self, num, window_num, items):
        """
        评价系统
        :param num: 客户号
        :param window_num: 窗口号
        :param items: 评价内容
        :return:
        """
        if not self.__eva_items.get(window_num):
            # 添加窗口到字典中，如果以及存在会自动跳过此步骤
            self.__eva_items.setdefault(window_num, {num: items})
        else:
            # 获取此窗口已经获得的评价
            dic = self.__eva_items[window_num]
            # 将新获得的评价填入其中
            dic.setdefault(num, items)
            # 将评价更新入评价表中
            self.__eva_items.update(dic)
        print('第', num, '客户对', window_num, '窗口的服务评价为：', items)

    # 输出所以评价
    @property
    def evas(self):
        return self.__eva_items


if __name__ == '__main__':
    windows = Queue()
    windows_vip = Queue()
    i = 1
    i_vip = 1
    eva = Eva()

    while True:
        print("-----------------------------------")
        a = input("""
                '选择操作'
                '1.客户端取号查号操作'
                '2.服务端评价后叫号'
                '3.查看当前正在运行的窗口以及正在处理的客户'
                '4.查看所以窗口的评价信息'
        """)
        if a == '1':
            cus = input("是否需要取号(输入y取号，不输入为只查看当前排队人数)")
            vip = input('是否为vip？（输入y为是）')
            if vip == 'y':
                print("当前有", len(windows_vip), '人正在排队')
                if cus == 'y':
                    print("您是第", i_vip, "号。尊敬的VIP您之前有", windows_vip.queueing(i_vip)[0:-1], '号，正在排队。')
                    i_vip += 1
            else:
                print("当前有", len(windows), '人正在排队号')
                if cus == 'y':
                    print("您是第", i, "号。您之前有", windows.queueing(i)[0:-1], '号，正在排队')
                    i += 1

        elif a == '2':
            window = input('请输入窗口号')
            if window == "vip":
                pop = windows_vip.pop()
                if pop > 1:
                    p = str(pop - 1) + '号VIP贵宾'
                    print(f"""请 {p} ，对VIP窗口进行业务评价。""")
                    n = input()
                    eva.eva_sys(p, "VIP窗口", n)
                print("请", pop, "号VIP贵宾在VIP窗口办理业务")
                eva.service('VIP窗口', pop)
            else:
                pop = windows.pop()
                window += '号窗口'
                if eva.dete(window):
                    p = str(pop - 1) + '号客户'
                    print(f"""请 {p} ，对{window}进行业务评价。""")
                    n = input()
                    eva.eva_sys(p, window, n)
                print('请', pop, '号客户,在', window, '，办理业务')
                eva.service(window, pop)

        elif a == '3':
            print(eva.services)

        elif a == '4':
            print(eva.evas)
