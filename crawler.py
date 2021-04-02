import re 
import urllib.request 
import time 
time.sleep(2) 
comment_list = [] 
for i in range(2): 
    url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn='+str(i)+'&type=17&oid=509127583637088413&sort=2' 
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' } 
    html = urllib.request.Request(url = url,headers = headers) 
    data = urllib.request.urlopen(html).read().decode('utf-8') 
    comment = re.findall(r'"content":{"message":"(.*?)"',data,re.S) 
    print(len(comment)) 
    comment_list.extend(comment) 
    print('评论已经爬取完成') 
comment_txt = open('comment.txt','w',encoding='utf-8') 
for r in comment_list: 
    comment_txt.write(r) 
comment_txt.close()