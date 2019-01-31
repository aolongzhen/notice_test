import datetime
import time

from common import class_log
from common import for_tocken
from common import http_requests

from common import class_mysql
from common.read_config import ReadConfig

#验证验证房间通知
class_log.Mylog().debug(msg="-----------验证房间活动通知------------", Handler=3)
#1.后台管理发起房间活动（开始时间为当前时间，结束时间为当前时间加+1天，其他随意，记录接口返回活动ID）
#2.启用刚创建的活动(创建时接口未返回id，so通过查询数据库查询出mic_task_id)
#3.用户进入房间（更具1，任何房间）
#4.查看提醒灯接口
#5.查看通知接口返回

send_time=int(round(time.time() * 1000))
add_url = ReadConfig(filepath='../notice.conf').read_config(section='ROOMKD_NOTICE',option='add_url')
param = ReadConfig(filepath='../notice.conf').read_config(section='ROOMKD_NOTICE',option='param')
param1=eval(param)
param1['begin_time']=time.strftime("%Y-%m-%d %H:%M", time.localtime())
param1['end_time']=(datetime.datetime.now()++datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
name='name'+str(send_time)
param1['name']=name
headers = ReadConfig(filepath='../notice.conf').read_config(section='ROOMKD_NOTICE',option='header')
result1 = http_requests.RequestsClass(url=add_url, param=param1, headers=eval(headers)).http_requests(method='post')
#查询数据
config = ReadConfig(filepath='../db_con.conf').read_config(section='DATABASE', option='config')
sql = 'select mic_task_id from activity_room_mic_task where name= %s'
data=(name,)
mic_task_id = class_mysql.DomysqlData(config=config, sql=sql, state=1, data=data).read_data()
print (mic_task_id)
#启用刚创建的活动
class_log.Mylog().debug(msg="-----------添加通知------------", Handler=3)
publish_url = ReadConfig(filepath='../notice.conf').read_config(section='ROOMKD_NOTICE',option='publish_url')
headers = ReadConfig(filepath='../notice.conf').read_config(section='ROOMKD_NOTICE',option='publish_header')
notice_id=mic_task_id
a = http_requests.RequestsClass(url=publish_url, param={"mic_task_id":mic_task_id}, headers=eval(headers)).http_requests(method='post')
class_log.Mylog().debug(msg="-----------发布通知-----------", Handler=3)

#用户进入房间
    #调用登录
tocken= for_tocken.ForTocken('18600000000')
    #进入房间
headers={'x-api-test': 'true','authorize-token': tocken,'app-version': '1.7.0'}
url='https://new-test-ck.haochang.tv/api/room/members'
param1={'roomId':tocken[1]}
result1 = http_requests.RequestsClass(url=add_url, param=param1, headers=eval(headers)).http_requests(method='post')
#调用监测点方法 验证结果

