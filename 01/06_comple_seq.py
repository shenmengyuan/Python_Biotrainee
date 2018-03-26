# -*- coding: utf-8 -*-
"""
@author: Shenmy
@contact: mengyuanshen@126.com
@file: 06_comple_seq.py
@time: 2018/1/4 10:12
@desc:
    对fasta文件取互补序列
"""

'''
解题思路：   
    构造碱基对的字典，需要注意的是N也要写进去；
    使用startwith()函数，判断是否是序列行，是的话是header行则输出，否的话是seq行则从碱基对字典中根据键查询值；
    查询写在for循环中，构造seq字符串，对序列每个碱基查询返回的值连起来，最后循环结束则输出互补序列。
'''

complement = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A', 'N': 'N'}
with open('test.fa') as f:
    for line in f:
        line_strip = line.strip()
        if line_strip.startswith('>'):
            print(line_strip, end="\n")
        else:
            seq = ''
            line_strip.upper()
            for i in line_strip:
                seq = seq + complement[i]
            print(seq, end="\n")

'''
### 参考资料
[菜鸟教程：Python3 字典](http://www.runoob.com/python3/python3-dictionary.html)
[](http://www.runoob.com/python3/python3-string-replace.html)

### 知识要点
1：对字典对象的学习；
2：replace方法一次只能完成一种替换，即某字符串替换成某字符串；（并不像perl中的tr/ATCG/TAGC/,能够一次完成多种替换）
'''
