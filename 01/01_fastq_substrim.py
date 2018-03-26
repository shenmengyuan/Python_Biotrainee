# -*- coding: utf-8 -*-
"""
@author: Shenmy
@contact: mengyuanshen@126.com
@file: 01_fastq_substrim.py
@time: 2017/12/14 21:28
@desc:
       5,3段截掉几个碱基
"""

# -----> pycharm有三种注释方式：
#            1.用 一对""" 括起来要注释的代码块。
#            2.用一对'''括起来要注释的代码块。
#            3.选中要注释的代码，按下ctrl+/注释。

# -----> 生成测试文件
# 安装bowtie2这个软件，里面有测试数据！
# ## Download and install bowtie
# cd ~/biosoft
# mkdir bowtie &&  cd bowtie
# wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.9/bowtie2-2.2.9-linux-x86_64.zip
# unzip bowtie2-2.2.9-linux-x86_64.zip
# head - n 8 longreads.fq > test.fq

# 按行读入fastq文件，避免内存爆满
# 每四行操作一次：
# 对第二行的序列和第四行的质量分别头尾截取掉n个，使用切片s[i:j]，可以写成s[n,-(n+1)]
# s代表要处理的字符串，i是开始截取的位置（从零开始的），j是终止的位置（可以是负的,后面开始没有0,所以要加1）
# 因为2、4列均是偶数，所以只需要加个记行数的标签，每次判断标签是否为偶数，如果是就进行切片，不是就输出


o = open('substrim_test.fq', 'w+')

with open('example/reads/test.fq') as f:
    count = 0
    for line in f:
        count += 1
        line_strip = line.strip()
        '''
        python去除空格和换行符的方法
        一、去除空格
        strip()
        "   xyz   ".strip()            # returns "xyz"  
        "   xyz   ".lstrip()           # returns "xyz   "  
        "   xyz   ".rstrip()           # returns "   xyz"  
        "  x y z  ".replace(' ', '')   # returns "xyz" 
        二、替换 replace("space","")
　　    用replace("\n", ""),后边的串替换掉前边的
        '''
        # print(line[5:-6])
         # print(line)
        if (count % 2) == 0:
            # print(line[5:-6])
            sub_line = line_strip[5:-6]
            print(sub_line, end='\n',  file=o)
        else:
            # print(line)
            print(line_strip, end='\n', file=o)

# 现在要把文件输出来到substrim_test.fq


