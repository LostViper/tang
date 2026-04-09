import re

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("有权裁定借款人", "有权将借款人划入")
text = text.replace("威压感的声音", "威势的声音")
text = text.replace("站在角落", "站在一旁")
text = text.replace("拉过一张锦凳", "搬过一张锦凳")
text = text.replace("落后的老爷车", "陈旧的老爷车")

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Fix 3 completed.")
