# -*- coding: utf-8 -*-
import os

filepath = '/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/42-第四十二章-甘特图下的奇迹与李泰护短.md'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(ch42_content)

print("Successfully wrote Chapter 42 directly.")
with open('/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/generate_ch42_direct3.py', 'r', encoding='utf-8') as f:
    exec(f.read())
