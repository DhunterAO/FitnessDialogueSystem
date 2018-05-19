import urllib.request
import pickle
import re
from pymongo import MongoClient
import pymongo


class Tool:
    RemoveImg = re.compile('<img.*?>| {7}|')
    # 匹配图片标签
    RemoveAddr = re.compile('<a.*?>|</a>')  # 匹配链接标签
    ReplaceLine = re.compile('<tr>|<div>|</div></p>')  # 匹配换行符的标签
    ReplaceTD = re.compile('<td>')  # 匹配制表符
    ReplacePara = re.compile('<p.*?>')  # 匹配段落开头
    ReplaceBR = re.compile('<br><br>|<br>')  # 匹配换行和双换行
    RemoveTag = re.compile('<.*?>')  # 匹配其余的标签

    def replace(self, x):
        x = re.sub(self.RemoveImg, "", x)  # 删除图片
        x = re.sub(self.RemoveAddr, "", x)  # 删除链接
        x = re.sub(self.ReplaceLine, "\n", x)  # 替换换行符
        x = re.sub(self.ReplaceTD, "", x)  # 将制表符替换
        x = re.sub(self.ReplacePara, "\n  ", x)  # 段落开头替换
        x = re.sub(self.ReplaceBR, "\n", x)
        x = re.sub(self.RemoveTag, "", x)  # 删除其余标签
        return x.strip()

class Muscle_lib:
    def __init__(self, url):
        self.url = url
        self.tool = Tool()
        self.file = None

    # 获取网页代码
    def gethtml(self):
        url = self.url
        request = urllib.request.Request(url)
        respones = urllib.request.urlopen(request)
        html = respones.read()
        html = html.decode('utf-8')
        file = open("html.txt", "w+")
        file.write(html)
        return html

    def get_muscle(self, html):
        pattern_muscle = re.compile('<span class="title">(.*?)</span></a>')
        muscle = re.findall(pattern_muscle, html)
        return muscle

    def start_muscle_related(self):
        # 开始爬取数据
        html = self.gethtml()
        # print("已获得源代码，正在处理......")
        muscle_action = self.get_muscle(html)

        return muscle_action


url = 'https://www.hiyd.com/dongzuo/1'
source = 'https://www.hiyd.com/dongzuo/'


client = MongoClient('localhost', 27017)
ActionDB = client.ActionDB
ActionTable = ActionDB.muscle
muscle_group = ['肱二头肌', '胸肌', '前臂', '中背部',
                '下背部', '颈部', '股四头肌', '腘绳肌',
                '小腿肌群', '肱三头肌', '斜方肌', '肩部', '腹肌', '臀部肌群',
                '内收肌群', '外展肌群', '背阔肌', '髂腰肌']
print(len(muscle_group))
add_group = []
for i in range(25):
    if i < 8 or i == 22:
        continue
    add_group.append(i)
add_group.append(26)
add_group.append(33)
url = 'http://www.hiyd.com/dongzuo/?muscle='
page = [4, 7, 2, 3, 2, 0, 13, 6, 5, 5, 2, 10, 12, 4, 0, 0, 9, 0]
print((add_group))

for i, element in enumerate(add_group):
    url_new = url + str(element)
    muscle_temp = []
    muscle = {}
    group_name = muscle_group[i]
    if page[i] != 0:
        for k in range(page[i]):
            url_newadd = url_new + '&page=' + str(k + 1)
            data = Muscle_lib(url_newadd)
            muscle_temp.append(data.start_muscle_related())
    else:
        url_newadd = url_new
        data = Muscle_lib(url_newadd)
        muscle_temp.append(data.start_muscle_related())
    muscle['name'] = muscle_group[i]
    muscle['muscleGroup'] = str(muscle_temp).replace('[', '').replace(']','').replace('\'','')
    ActionTable.insert_one(muscle)
