#!/usr/bin/python
#coding:utf-8






import re
def getwebinfo(html):
    html=html.lower()

    result={}
    result['keywords']=''
    regex = "(?<=meta name=\"keywords\" content=\").*?(?=\")"

    reobj = re.compile(regex)
    match = reobj.search(html)
    if match:
        result['keywords']= match.group()
    else:


        regex = "(?<=meta http-equiv=\"keywords\" content=\").*?(?=\")"

        reobj = re.compile(regex)
        match = reobj.search(html)
        if match:
            result['keywords']= match.group()

    regex="(?<=<title>).*?(?=</title>)"
    reobj = re.compile(regex)
    match = reobj.search(html)
    if match:
        result['title']= match.group()
    else:
        result['title']=''



    return result

def getcode(url):

    import chardet

    import urllib
    result='unknow'
    try:
        data1 = urllib.urlopen(url).read()

        chardit1 = chardet.detect(data1)
        result=chardit1['encoding']
    except Exception,e:
        print e
    return result
if __name__ == "__main__":
    import connecttool
    a=connecttool.ConnectTool()
    head,keywords=a.getHTML('http://www.biquge.com',way='GET',params={},times=1)


    k= getwebinfo(keywords)
    print k['keywords'],k['title']