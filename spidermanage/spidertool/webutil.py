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
    return result


if __name__ == "__main__":
    import connecttool
    a=connecttool.ConnectTool()
    head,keywords=a.getHTML('http://www.ytu.edu.cn',way='GET',params={},times=1)


    k= getwebinfo(keywords)
    print k['keywords']