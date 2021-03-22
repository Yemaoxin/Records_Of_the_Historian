import json
import  re
_MAPPING = [u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七',u'十八', u'十九']

mode=re.compile('（.*）')
def _to_chinese4(num):
    str_num = ''
    if(num>100):
        str_num+=_MAPPING[num//100]+'百'
        num=num%100
        ten=num//10
        str_num+=_MAPPING[ten]
        if(ten!=0):
            str_num+='十'
        if(num%10!=0):
          str_num+=_MAPPING[num%10]
    elif (num==100):
        str_num='一百'
    elif (num>=20):
        str_num=_MAPPING[num//10]+'十'
        if(num%10!=0):
            str_num+=_MAPPING[num%10]
    else:
        str_num=_MAPPING[num]
    return str_num

if __name__ =='__main__':
    print(_to_chinese4(110))
    print(_to_chinese4(107))
    print(_to_chinese4(100))
    print(_to_chinese4(83))
    book = {}
    with open('白话史记') as f:
        ff = open('白话史记_sentence', 'w')
        lines = f.readlines()
        num = 1
        topic_name = ''
        count=0
        for line in lines:
            if (line == '\n'):
                continue
            if(num<=22 and count==0):
               str_count = '卷{}'.format(_to_chinese4(num))
            else:
                str_count = '卷{}'.format(_to_chinese4(num+1))

            if (str_count in line):
                topic_name = line.split(' ')[1].split('第')[0]
                topic_name = '第{}章 '.format(num) + topic_name
                num += 1
                print(str_count)
                if(num==23 and count==0):
                    num=22
                    count=1
                    continue
                book[topic_name] = []
                ff.write(topic_name + '\n')
            else:
                line = re.sub(mode, '', line, count=0)
                line = line.replace('\n', '')
                for sentence in line.split('。', -1):
                    if (sentence == ''):
                        continue
                    book[topic_name].append(sentence + '。')
                    ff.write(sentence + '。\n')
        ff.close()
    print(len(book.items()))
    with open('baihua_shiji.json', 'w') as f:
        f.write(json.dumps(book, ensure_ascii=False))





