# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 23:52:29 2017

@author: Shenmy
"""

import os
from collections import OrderedDict # # 从collections模块中导入OrderedDict


os.chdir('D:/Python_learning/slice_sequence') # 设置工作目录

chr_dict = OrderedDict()  # 定义一个有序字典
tmp_chr = '' 
with open('raw_sequence.txt', 'r') as raw:
    for line in raw:
        line = line.strip()
        if line.startswith('>'):
            temp_chr = line  # 将序列名称储存至字典变量中
            chr_dict[temp_chr] = ''
        else:
            chr_dict[temp_chr] += line  # 将序列储存至字典变量

s = '_'
f = open('raw_sequence_slice.fa', 'w+')
for seqnames, seq in chr_dict.items():
    length = len(seq)
    a =0 
    star = 0
    for i in range(star, length, 1499):
        a = a + 1 
        substr = seq[i:1999+i]
        header = seqnames + str(s) + str(a)
        print(header, substr, sep='\n', file=f)

