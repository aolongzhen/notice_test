import datetime
import time
from common import for_tocken
from common import http_requests
from common import class_mysql
from common.read_config import ReadConfig
import  check_point
#验证验证房间通知
#class_log.Mylog().debug(msg="-----------验证房间活动通知------------", Handler=3)
#1.后台管理发起房间活动（开始时间为当前时间，结束时间为当前时间加+1天，其他随意，记录接口返回活动ID）
#2.启用刚创建的活动(创建时接口未返回id，so通过查询数据库查询出mic_task_id)
#3.用户进入房间（更具1，任何房间）
#4.查看提醒灯接口
#5.查看通知接口返回
'''
send_time=int(round(time.time() * 1000))
add_url = ReadConfig(filepath='../conf/notice.conf').read_config(section='ROOMKD_NOTICE',option='add_url')
param = ReadConfig(filepath='../conf/notice.conf').read_config(section='ROOMKD_NOTICE',option='param')
param1=eval(param)
param1['begin_time']=time.strftime("%Y-%m-%d %H:%M", time.localtime())
param1['end_time']=(datetime.datetime.now()++datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
name='name'+str(send_time)
param1['name']=name
headers = ReadConfig(filepath='../conf/notice.conf').read_config(section='ROOMKD_NOTICE',option='header')
result1 = http_requests.RequestsClass(url=add_url, param=param1, headers=eval(headers)).http_requests(method='post')
#查询数据
config = ReadConfig(filepath='../conf/db_con.conf').read_config(section='DATABASE', option='config')
sql1 = 'select mic_task_id from activity_room_mic_task where name= %s'
data=(name,)
mic_task_id = class_mysql.DomysqlData(config=config, sql=sql1, state=1, data=data).read_data()
print (mic_task_id)
print (mic_task_id[0][0])

#启用刚创建的活动
#class_log.Mylog().debug(msg="-----------添加通知------------", Handler=3)
publish_url = ReadConfig(filepath='../conf/notice.conf').read_config(section='ROOMKD_NOTICE',option='publish_url')
headers = ReadConfig(filepath='../conf/notice.conf').read_config(section='ROOMKD_NOTICE',option='publish_header')
a = http_requests.RequestsClass(url=publish_url, param={"mic_task_id":'275'}, headers=eval(headers)).http_requests(method='post')
print (a)
#class_log.Mylog().debug(msg="-----------发布通知-----------", Handler=3)
'''
#调用登录
#进入房间
config = ReadConfig(filepath='../conf/db_con.conf').read_config(section='DATABASE', option='config')
telphone='18600000001'
tocken= for_tocken.ForTocken(telphone).return_tocken()
print (tocken[2])
headers={'x-api-test': 'true','authorize-token': tocken[0],'app-version': '1.7.0'}
url='https://new-test-ck.haochang.tv/api/room/members'
result1 = http_requests.RequestsClass(url=url, param={'roomId':tocken[1]}, headers=headers).http_requests(method='post')
#查询notice_id
sql2 ='select id from activity_mic_task_user_notice t  where t.user_id=%s  and t.detail_id=%s'
data=(tocken[2],275)
notice_id =class_mysql.DomysqlData(config=config, sql=sql2, state=1, data=data).read_data()
print(notice_id)
#调用监测点方法 验证结果
#check_point.CheckPoint(notice_id=notice_id,send_time=send_time,tocken=tocken[0])