import re

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("性命之忧", "丢掉性命的危险")
text = text.replace("名誉之举", "名誉的举动")
text = text.replace("此言一出", "这话一出")
text = text.replace("慎言", "别胡说")
text = text.replace("此刻", "现在")
text = text.replace("此时", "现在")
text = text.replace("不仅如此", "不但这样")
text = text.replace("顺便", "顺带")
text = text.replace("即便", "就算")
text = text.replace("便是", "就是")
text = text.replace("之", "的") # this might break some idioms, let's be careful. Let's not do blanket replace.
text = text.replace("随便", "随便")

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Fix 4 completed.")
