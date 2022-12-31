# -*- coding: utf-8 -*-
'''
@File    :   hw1.py
@Time    :   2022/12/17 21:29:55
@Author  :   Yishu Zhou 
'''
# Start typing your code from here
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
# python parser_arg.py --lines=5 alpha.txt beta.txt