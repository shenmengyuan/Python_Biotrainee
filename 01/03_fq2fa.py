# -*- coding: utf-8 -*-
"""
@author: Shenmy
@contact: mengyuanshen@126.com
@file: 03_fq2fa.py
@time: 2017/12/17 15:26
@desc:
    FASTQ 转换成 FASTA
"""
'''
解题思路：
        关键点在于每次读入四行，输出第一行和第二行；
        中间还可以对第一行header进行替换操作，把"@"换成">"
'''
o = open('test.fa', 'w+')

with open('example/reads/test.fq') as f:
    while True:
        # 读入->去空格->替换 可以一行完成，方法可以叠加
        header = f.readline().strip().replace('@', '>')
        # print(header)
        if not (header and f):
            # 当读入的文件中没有值给header时，就会是终止while循环
            break
        seq = f.readline().strip()
        com = f.readline().strip()
        quality = f.readline().strip()

        # print(header)
        # print(seq)
        print(header, file=o)
        print(seq, file=o)

'''
思考：
    浩浩说.readline()只适合用于读小文件，那么对于大文件来说应该怎么操作呢？
    暂时还没有啥想法，以后再解决了哦
'''
