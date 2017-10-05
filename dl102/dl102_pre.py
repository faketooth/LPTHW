# -*- coding: utf-8 -*-
import codecs
import jieba

with codecs.open('happiness_seg.txt', 'rb', encoding='utf-8') as f:
    info = f.read()

info = info.replace("\n", ',')
seg_list = jieba.cut(info, cut_all=True)

word_list = []

for word in seg_list:
    if word in [' ', '']:
        continue
    word_list.append(word)

count = {}
for i in xrange(len(word_list)-1):
    pair = (word_list[i], word_list[i+1])
    current = count.get(pair)
    if current:
        count[pair] = current + 1
    else:
        count[pair] = 1

top10 = sorted(count, key=count.__getitem__, reverse=True)[:10]

for k in top10:
    print k[0], k[1], count[k]
