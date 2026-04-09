import re

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("只见程处弼", "程处弼")

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Fix 6 completed.")
