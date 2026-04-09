# -*- coding: utf-8 -*-
import os

with open('part1_2.py', 'r', encoding='utf-8') as f:
    exec(f.read())

with open('part3_4.py', 'r', encoding='utf-8') as f:
    exec(f.read())

filepath = '/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/40-第四十章-立政殿献币与皇家银行挂牌.md'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(part1_2_content + "\n" + part3_4_content)

print("Successfully generated and written Chapter 40.")