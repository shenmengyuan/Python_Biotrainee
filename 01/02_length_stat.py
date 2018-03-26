# -*- coding: utf-8 -*-
"""
@author: Shenmy
@contact: mengyuanshen@126.com
@file: 02_length_stat.py
@time: 2017/12/15 21:15
@desc:
    序列长度分布统计：总长、平均值、最长、最短长度分别是多少
"""

'''
解题思路：
    1：使用len()得到每条序列的长度，任意选择第序列行或者质量行，存为一个列表；
    2：使用mean()/max()/min()函数或者类似函数返回长度的统计值；
'''
# 使用numpy包
import numpy

# 构造一个空的列表
lens = []
len_sum = 0
# 读入文件
with open('example/reads/test.fq') as f:
    count = 0
    for line in f:
        count += 1
        line_strip = line.strip()
        if (count % 4) == 0:  # 判断是否是质量行，接着用len()统计长度
            length = len(line_strip)
            # len_sum = len_sum + length
            lens.append(length)   # 每遇到一次质量行统计长度后把长度值加到lens列表中

# 使用numpy包中的sum()/mean()/min()函数对lens列表进行统计：
    Sum = numpy.sum(lens)
    Mean = numpy.mean(lens)
    Min = numpy.min(lens)
# 使用len()函数对lens列表计算元素个数
    Num = len(lens)

    print("Sum", Sum, sep=":")
    print("Mean", Mean, sep=":")
    print("Min", Min, sep=":")
    print("Num", Num, sep=":")

