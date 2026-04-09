import re

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "r", encoding="utf-8") as f:
    text = f.read()

# Make sure all forbidden words are replaced correctly
text = text.replace("落了厚厚一层白", "覆了厚厚一层白")
text = text.replace("被压迫的旧势力", "被逼到绝路的旧势力")
text = text.replace("话音未落", "话还未说完")
text = text.replace("有权判定借款人", "有权裁定借款人")
text = text.replace("可怕压迫感的声音", "可怕威压感的声音")
text = text.replace("落在柴哲威", "扫过柴哲威")
text = text.replace("像一头被困", "犹如一头被困")
text = text.replace("落人口实", "授人以柄")
text = text.replace("压住了屋内", "镇住了屋内")
text = text.replace("工业底盘", "工业根基")
text = text.replace("信用评级", "信用体系")
text = text.replace("绝对资本碾压能力", "绝对资本手段")
text = text.replace("压得极低", "放得极低")
text = text.replace("像是从牙缝里", "犹如从牙缝里")
text = text.replace("拉到了解体的边缘", "推到了解体的边缘")
text = text.replace("全压下了", "全留中不发了")

with open("/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/11-章节草稿/48-第四十八章-反派的狂欢与苏醒的降维反杀.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Fix completed.")
