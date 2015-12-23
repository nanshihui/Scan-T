
#!/usr/bin/python
#coding=utf-8

import time,datetime
import re
import webtool
from TaskTool import TaskTool
import os
import config
import json,SQLTool,Sqldatatask,Sqldata
getlocationtaskinstance=None
def getObject():
    global getlocationtaskinstance
    if getlocationtaskinstance is None:
        getlocationtaskinstance=GetLocationTask(1)
    return getlocationtaskinstance
def getlocationjsondata(jsondata):
    print jsondata
    if jsondata.get('code','1')==0:
        country=jsondata['data'].get('country','0')
        country_id=str(jsondata['data'].get('country_id','0'))
        area=jsondata['data'].get('area','0')
        area_id=str(jsondata['data'].get('area_id','0'))
        region=jsondata['data'].get('region','0')
        region_id=str(jsondata['data'].get('region_id','0'))
        city=jsondata['data'].get('city','0')
        city_id=str(jsondata['data'].get('city_id','0'))
        county=jsondata['data'].get('county','0')
        county_id=str(jsondata['data'].get('county_id','0'))
        isp=jsondata['data'].get('isp','0')
        isp_id=str(jsondata['data'].get('isp_id','0'))
        return country,country_id,area,area_id,region,region_id,city,city_id,county,county_id,isp,isp_id
    else:
        return '0','0','0','0','0','0','0','0','0','0','0','0'

class GetLocationTask(TaskTool):
    def __init__(self,isThread=1,deamon=True):
        TaskTool.__init__(self,isThread,deamon=deamon)
        
        self.sqlTool=Sqldatatask.getObject()

        self.config=config.Config
        self.set_deal_num(1)
    def task(self,req,threadname):
        print 'the ip is '+req
        ip=req
        jsondata=webtool.getLocationinfo(req)
        country,country_id,area,area_id,region,region_id,city,city_id,county,county_id,isp,isp_id=getlocationjsondata(jsondata)
        localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
        insertdata=[]
        

        insertdata.append((ip,country,country_id,area,area_id,region,region_id,city,city_id,county,county_id,isp,isp_id,localtime))
                                         
        extra=' on duplicate key update  updatetime='+SQLTool.formatstring(localtime)+',country='+SQLTool.formatstring(country)+', country_id='+SQLTool.formatstring(country_id)+',area='+SQLTool.formatstring(area)+', area_id='+SQLTool.formatstring(area_id)+',region='+SQLTool.formatstring(region)+', region_id='+SQLTool.formatstring(region_id)+',city='+SQLTool.formatstring(city)+', city_id='+SQLTool.formatstring(city_id)+',county='+SQLTool.formatstring(county)+', county_id='+SQLTool.formatstring(county_id)+',isp='+SQLTool.formatstring(isp)+', isp_id='+SQLTool.formatstring(isp_id)

        sqldatawprk=[]
        dic={"table":self.config.iptable,"select_params":['ip','country','country_id','area','area_id','region','region_id','city','city_id','county','county_id','isp','isp_id','updatetime'],"insert_values":insertdata,"extra":extra}
        tempwprk=Sqldata.SqlData('inserttableinfo_byparams',dic)
        sqldatawprk.append(tempwprk)
        self.sqlTool.add_work(sqldatawprk)
        
        time.sleep(0.1)
        ans=''
        return ans
#        
#{"code":0,"data":{"country":"\u4e2d\u56fd","country_id":"CN",
#                   "area":"\u534e\u5317","area_id":"100000",
#                   "region":"\u5317\u4eac\u5e02","region_id":"110000",
#                   "city":"\u5317\u4eac\u5e02","city_id":"110100",
#                   "county":"","county_id":"-1",
#                   "isp":"\u8054\u901a","isp_id":"100026",
#                   "ip":"123.123.123.123"
#                   }
#}
#
def test():
    jsondata=webtool.getLocationinfo('123.123.123.123')
    if jsondata.get('code','1')==0:
        country=jsondata['data'].get('country','0')
        country_id=str(jsondata['data'].get('country_id','0'))
        area=jsondata['data'].get('area','0')
        area_id=str(jsondata['data'].get('area_id','0'))
        region=jsondata['data'].get('region','0')
        region_id=str(jsondata['data'].get('region_id','0'))
        city=jsondata['data'].get('city','0')
        city_id=str(jsondata['data'].get('city_id','0'))
        county=jsondata['data'].get('county','0')
        county_id=str(jsondata['data'].get('county_id','0'))
        isp=jsondata['data'].get('isp','0')
        isp_id=str(jsondata['data'].get('isp_id','0'))
        return country,country_id,area,area_id,region,region_id,city,city_id,county,county_id,isp,isp_id

if __name__ == "__main__":

    a=getObject()
    a.add_work(['www.baidu.com'])
    while True:
        pass


