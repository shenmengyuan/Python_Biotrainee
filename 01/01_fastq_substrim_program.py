# -*- coding: utf-8 -*-
"""
@author: Shenmy
@contact: mengyuanshen@126.com
@file: 01_fastq_substrim_program.py.py
@time: 2018/3/26 10:16
@desc:
"""
import argparse


def sub_trim(infile, outfile, left_trim, right_trim):
    o = open(outfile, 'w+')
    with open(infile) as f:
        count = 0
        for line in f:
            count += 1
            line_strip = line.strip()
            if (count % 2) == 0:
                sub_line = line_strip[left_trim:-right_trim]
                print(sub_line, end='\n', file=o)
            else:
                print(line_strip, end='\n', file=o)


def get_args():
    """
    get args
    :return:
    """
    args = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                   description="""
description:
    Trim the FastAQ files

author:  ShenMengyuan (mengyuanshen@126.com)
        """)

    args.add_argument("-i", "--input", metavar="FASTQ", help="input fastq files")
    args.add_argument("-o", "--output", default="subtrim.fq", metavar="FASTQ", help="output fastq files")
    args.add_argument("-l", "--left_len", type=int, metavar="INT", default=0, help="left length to trim")
    args.add_argument("-r", "--right_len", type=int, metavar='INT', default=0, help="right length to trim")

    return args.parse_args()


def main():
    args = get_args()
    sub_trim(args.input, args.output, args.left_len, args.right_len)


if __name__ == "__main__":
    main()
