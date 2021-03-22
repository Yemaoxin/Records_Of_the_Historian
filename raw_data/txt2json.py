import jiayan
import json
book={}
with open('shiji.txt') as f:
    ff=open('shiji_sentence','w')
    lines=f.readlines()
    new_topic=False
    num=0
    topic_name=''
    for line in lines:
        # 每一章节开头的标记
        if('-------' in line):
            new_topic=True
            num+=1
        else :
            # 去除空格
            if(line=='\n'):
                continue
            if('第{}章'.format(num) in line and new_topic):
                line=line.replace('\n','')
                book[line]=[]
                topic_name=line
                ff.write(topic_name+'\n')
            else :
                line=line.replace('\t','')
                line=line.replace(' ','')
                line=line.replace('\n','')
                for sentence in line.split('。',-1):
                    if(sentence==''):
                        continue
                    book[topic_name].append(sentence+'。')
                    ff.write(sentence+'。\n')
    ff.close()


with open('Shiji.json', 'w') as f:
    f.write(json.dumps(book,ensure_ascii=False))

