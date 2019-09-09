# -*- coding: UTF-8 -*-
from pkuseg import pkuseg
from collections import Counter

f = open("23863-0.txt", encoding="utf-8")
content = f.read()

seg = pkuseg()
words = seg.cut(content)

text = [word for word in words if len(word) > 1]

counter = Counter(text)
top = counter.most_common(50)
for word in top:
    print(word[0], word[1])

