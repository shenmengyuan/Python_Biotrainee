# -*- coding: utf-8 -*-
"""
@author: Shenmy
@contact: mengyuanshen@126.com
@file: 04_CG_count.py
@time: 2017/12/23 23:22
@desc:
    统计碱基个数及GC%
"""

'''
解题思路：
    碱基个数统计则是需要分别对A/T/C/G碱基进行数个数叠加（可能存在N,这里就先不考虑它了）；
    GC含量就是G/C的碱基数之和除以A/T/C/G的碱基总和；
    关键就是对四种碱基进行个数统计，使用.count；
    # fastqc的统计结果：%GC:59
'''

Sum_G = 0
Sum_C = 0
Sum_A = 0
Sum_T = 0
with open('./example/reads/test.fq') as f:
    while True:
        header = f.readline().strip()
        if not (header and f):
            # 当读入的文件中没有值给header时，就会是终止while循环
            break
        seq = f.readline().strip().upper()  # 把所有字母变成大写
        com = f.readline().strip()
        quality = f.readline().strip()
        Sum_G = seq.count("G") + Sum_G
        Sum_C = seq.count("C") + Sum_C
        Sum_A = seq.count("A") + Sum_A
        Sum_T = seq.count("T") + Sum_T

GC = (Sum_G + Sum_C)/(Sum_G + Sum_C + Sum_A + Sum_T)
print("Sum_A", Sum_A, sep=":")
print("Sum_T", Sum_T, sep=":")
print("Sum_C", Sum_C, sep=":")
print("Sum_G", Sum_G, sep=":")
print("GC", GC, sep=":")


'''
结果与fastqc的结果一样：
                    Sum_A:102
                    Sum_T:105
                    Sum_C:149
                    Sum_G:149
                    GC:0.5900990099009901
'''

# 最后是PyCharm与服务器的代码同步：
# https://www.cnblogs.com/sherry-song/p/5358349.html
