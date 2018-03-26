# -*- coding: utf-8 -*-
"""
@author: Shenmy
@contact: mengyuanshen@126.com
@file: 05_read_largrfile.py
@time: 2017/12/27 9:42
@desc:
        读取大文件方法探索：
        - 公众号读者留言linecache模块
        - readline()
        - readlines()
        - for line in f:
"""

import linecache

# 获取全部内容
a = linecache.getlines('example/reads/longreads.fq')
print(len(a))

# 获取1到4行内容
b = linecache.getlines('example/reads/longreads.fq')[0:4]
for line in b:
    print(line.strip())

# 获取第四行内容
# c = linecache.getline('example/reads/longreads.fq', 4)


'''
linecache这模块并不是我所需要的，因为它使用内存来缓存文件内容，是很耗内存的。
并不能解决用小内存的电脑处理大文件，之前看dongye师兄的python视频是应该把文件分块读入缓存进行操作的。

with open('example/reads/test.fq', 'r') as f:
    while 1:
        line = f.readline() # 每次读取一行
        if not line:
          break
        ## do something

with open('example/reads/test.fq', 'r') as f:
    for line in f.readlines(): # 一次性把所有数据读取到内存
     ## do something
     
with open('example/reads/test.fq', 'r') as f:
    for line in f:    # 最快、最安全的方式
      ## do something

'''