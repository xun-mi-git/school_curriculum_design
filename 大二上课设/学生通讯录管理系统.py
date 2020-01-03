# /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/12/30 12:59
# @Author  : 寻觅
# @File    : 学生通讯录管理系统. py
# @Software: PyCharm

import pymysql

"""
①输入数据建立通讯录。建立通讯录系统，可以一次输入多个成员通讯录的信息，建立通讯录；
②查询通讯录中满足要求的信息。分别按2种方式查询所需要的通讯录成员记录，一是按学号，二是按姓名；
③插入新的通讯录信息。每次可以插入一个成员通讯录的信息，如果要连续插入多个成员通讯录信息则必须多次选择该功能；
④删除不需要的通讯录信息。可按3种方式进行删除，分别：按序号删除、按学号删除和按姓名删除；
⑤查看所有的通讯录信息。显示通讯录中所有成员信息。
"""


class Table:
    # 初始化
    def __init__(self):
        # 连接数据库
        self.__mysql = pymysql.connect(host='129.211.85.3', port=3306, db='学生管理系统', user='xunmi', passwd='8GE8+1ge1',
                                       charset='utf8')
        # 创建游标
        self.__cur = self.__mysql.cursor()

    # 将方法伪装为属性的装饰器
    @property
    def all(self):
        """读取所有信息"""
        self.__cur.execute("select 序号, 学号, 姓名, 联系方式 from 学生联系方式;")
        return self.__cur.fetchall()

    def add(self, num, name, contact):
        """
        添加信息
        :param num: 学号
        :param name: 姓名
        :param contact: 联系方式
        :return:
        """
        # 使用的MySQL为Innodb存储引擎，支持事务，pymysql会自动启动事务
        self.__cur.execute("insert into 学生联系方式 values(%d, '%s', '%s', 0);" % (num, name, contact))
        # 提交事务
        self.__mysql.commit()

    def lookup(self, header, tables):
        """
        查找信息
        :param header: 指定查找的序列
        :param tables: 查找的内容
        :return: 输出已找到的内容
        """
        self.__cur.execute("select 序号, 学号, 姓名, 联系方式 from 学生联系方式 where %s='%s';" % (header, tables))
        return self.__cur.fetchall()

    def pop(self, header, tables):
        """
        删除信息
        :param header: 指定查找的序列
        :param tables: 删除的内容
        :return: 输出已找到的内容
        """
        self.__cur.execute("delete from 学生联系方式 where %s='%s';" % (header, tables))
        # 提交事务
        self.__mysql.commit()

    @property
    def repeats(self):
        sure = input("是否继续程序？（输入y继续）")
        if sure != 'y':
            return False
            # 清除游标
            self.__cur.close()
            self.__mysql.close()
        return True


# 主程序
if __name__ == '__main__':
    # 实例化类
    data = Table()
    repeat = True
    while repeat:
        # 界面选择
        print("""
            1.输出所以信息
            2.添加新的数据
            3.查找信息
            4.删除信息
        """)
        a = input("请输入需要执行的功能")
        if a == "1":
            data_all = [i for i in data.all]
            print('序号 --- 学号 --- 姓名 --- 联系方式')
            for i in data_all:
                print(i)
            repeat = data.repeats

        if a == "2":
            new_data = input("请按顺序输入一下信息->学号,姓名,联系方式<-用空格隔开\n")
            new_list = new_data.split(' ')
            new_list[0] = int(new_list[0])
            print('您输入的信息是：', new_list)
            data.add(new_list[0], new_list[1], new_list[2])
            repeat = data.repeats

        if a == "3":
            header_data = ['学号', '姓名']
            header_num = int(input('查找方式（输入数字）1.学号,2.姓名：')) - 1
            tables_data = input('查找内容：')
            look = data.lookup(header_data[header_num], tables_data)[0]
            print('您查找的学生\n序号：', look[0], '\n学号：', look[1], '\n姓名：', look[2], '\n联系方式：', look[3], '\n')
            repeat = data.repeats

        if a == "4":
            header_data = ['学号', '姓名', '序号']
            header_num = int(input('指定方式（输入数字）1.学号,2.姓名,3.序号。')) - 1
            tables_data = input('删除内容')
            data.pop(header_data[header_num], tables_data)
            repeat = data.repeats




