import json
import jieba
with  open('Shiji.json') as f:
    book=json.loads(f.read())
with open('baihua_shiji.json') as f:
    baihua_book=json.loads(f.read())
jieba.load_userdict('史记词典.txt')

# +++++++++
chapter_name='第2章 夏本纪'
# +++++++++

# 白话和文言的单章分词文件

with open('temp_baihua','w') as f:
    for i in range(0,  len(baihua_book[chapter_name])):
        if (i < len(baihua_book[chapter_name])):
            for i in list(jieba.cut(baihua_book[chapter_name][i])):
                f.write(i+'  ')
            f.write('\n')
with open('temp_shiji','w') as f:
    for i in range(0,len(book[chapter_name])):
        if (i < len(book[chapter_name])):
            for i in list(jieba.cut(book[chapter_name][i])):
                f.write(i+'  ')
            f.write('\n')



