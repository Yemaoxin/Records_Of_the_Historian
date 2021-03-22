import json
import pathlib
from shutil import copyfile
author_name='ye11'
# kk 、cc
file_name=author_name+'_shiji_dict.json'
if(not pathlib.Path(file_name).exists()):
    copyfile('shiji_dict.json',file_name)
if __name__=='__main__':
    with open(file_name) as f:
        shiji_dict=json.loads(f.read())
    print(author_name+'正在编辑:')
    word=''
    while(word!='-1'):
        word=input("输入古文词\n")
        if(word=='-1'):
            break
        if(word==''):
            continue
        if(word in shiji_dict.keys()):
            print('已经有该词了')
            print('是否重写该词')
            x=input('输入1重写\n')
            if(x=='1'):
                new_value=input('输入新的现代中文词')
                shiji_dict[word]=new_value
            continue
        value=input('输入现代中文词\n')
        shiji_dict[word]=value
    print("现已有词表长度:",len(shiji_dict.keys()))
    with open(file_name,'w') as f:
        f.write(json.dumps(shiji_dict,ensure_ascii=False))

