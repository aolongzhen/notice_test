#1.登录后台生成session


from common import http_requests

url='http://new-test.ck.haochang.tv/admin/login'
param={'account':'admin','password':'admin','platform':'party'}
header={"X-HTTP-Method-Override":"POST","Referer": "http://new-test.ck.haochang.tv/admin/login"}
result=http_requests.RequestsClass(url=url, param=param,headers=header).http_requests(method='post')
session1=(result.cookies.get_dict())
session = {'cookie':'PHPSESSID='+session1['PHPSESSID']}
