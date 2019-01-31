import time

from common import http_requests

from common import class_log, read_config

#验证官方通知
class_log.Mylog().debug(msg="-----------验证官方通知------------", Handler=3)

#请求后台管理接口生成通知
#添加通知
send_time=int(round(time.time() * 1000))

add_url = read_config.ReadConfig(filepath='notice.conf').read_config(section='SYS_NOTICE', option='add_url')
param = read_config.ReadConfig(filepath='notice.conf').read_config(section='SYS_NOTICE', option='param')
headers = read_config.ReadConfig(filepath='notice.conf').read_config(section='SYS_NOTICE', option='header')
result1 = http_requests.RequestsClass(url=add_url, param=eval(param), headers=eval(headers)).http_requests(method='post')
class_log.Mylog().debug(msg="-----------添加通知------------", Handler=3)

#发布通知
publish_url = read_config.ReadConfig(filepath='notice.conf').read_config(section='SYS_NOTICE', option='publish_url')
notice_id=result1.json()['sys_notice_id']
a = http_requests.RequestsClass(url=publish_url, param=result1.json(), headers=eval(headers)).http_requests(method='post')
class_log.Mylog().debug(msg="-----------发布通知-----------", Handler=3)

#缺少redis操作，删除提醒灯


