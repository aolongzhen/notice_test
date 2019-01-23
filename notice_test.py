import http_requests
import read_config

#验证官方通知
#请求后台管理接口生成通知
#添加通知
add_url = read_config.ReadConfig(filepath='notice.conf').read_config(section='SYS_NOTICE',option='add_url')
param = read_config.ReadConfig(filepath='notice.conf').read_config(section='SYS_NOTICE',option='param')
headers = read_config.ReadConfig(filepath='notice.conf').read_config(section='SYS_NOTICE',option='header')
result = http_requests.RequestsClass(url=add_url, param=param, headers=headers).http_requests(method='post')

#发布通知
publish_url = read_config.ReadConfig(filepath='notice.conf').read_config(section='SYS_NOTICE',option='publish_url')
a = http_requests.RequestsClass(url=publish_url, param=param, headers=headers).http_requests(method='post')


