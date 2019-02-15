#后台发送官方通&发布通知

from common import  read_config,http_requests,login_management
from conf import project_path
import time

#调用后台登录获得session
session =login_management.session

t=int(round(time.time() * 1000))
#添加通知
readconfig=read_config.ReadConfig(filepath=project_path.notice_file)
add_url = readconfig.read_config(section='SYS_NOTICE', option='add_url')
param = readconfig.read_config(section='SYS_NOTICE', option='param')
base_header= readconfig.read_config(section='SYS_NOTICE', option='header')
headers=dict(eval(base_header),**session)
result1 = http_requests.RequestsClass(url=add_url, param=eval(param), headers=headers).http_requests(method='post')

#发布通知
publish_url = readconfig.read_config(section='SYS_NOTICE', option='publish_url')
notice_id=result1.json()['sys_notice_id']
print (notice_id)
a = http_requests.RequestsClass(url=publish_url, param=result1.json(), headers=headers).http_requests(method='post')

#redis操作，删除对应用户ID：11373864提醒灯
#do_redis.DoRedis('user:notification:11373864').del_key()