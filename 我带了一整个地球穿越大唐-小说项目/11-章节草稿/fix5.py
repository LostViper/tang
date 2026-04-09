import re

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("断言", "那句话")
text = text.replace("留言", "留话")
text = text.replace("无言以对", "说不出话")
text = text.replace("无言", "没话")
text = text.replace("的举动", "的行为") # cleanup from earlier just in case
text = text.replace("无言以对", "说不出话")

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Fix 5 completed.")
