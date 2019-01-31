#传入参数telephone，根据传入参数查找tocken，如果没有找到则登录生成并写入文件
#取文件中tocken使用，测试请求，如果请求成功则返回tocken。如果请求报错（tocken错误）则重新登录生成tocken 并更新文件内容

import base64
from common import http_requests
from common import read_txt


class ForTocken():
        def __init__(self,telephone):
            self.telephone=telephone

        def again_log(self):
            url = 'https://new-test-ck.haochang.tv/api/captcha/telphone'
            param = {'telphone': self.telephone}
            headers = {'x-api-test': 'true'}
            http_requests.RequestsClass(url=url, param=param, headers=headers).http_requests(method='get')
            url = 'https://new-test-ck.haochang.tv/api/login/telphone'
            param = {'telphone': self.telephone, 'captcha': '1234'}
            req_data = http_requests.RequestsClass(url=url, param=param, headers=headers).http_requests(method='post')
            tocken = req_data.json()['authorizeToken']
            roomid = req_data.json()['data']['room']['roomId']
            return [tocken,roomid]

        def toc_base(self,tocken):
            tocken= str(base64.b64encode(bytes(tocken, encoding = "utf8")), encoding = "utf-8")
            return tocken

        def return_tocken(self):
            data=eval(read_txt.DoTxt('../data/log_tocken.txt').read_txt())
            if self.telephone in data.keys():
                headers = {'x-api-test': 'true','authorize-token': self.toc_base(data[self.telephone][0])}
                url='https://new-test-ck.haochang.tv/api/accompany/db'
                req_data = http_requests.RequestsClass(url=url, param={}, headers=headers).http_requests(method='get')
                if req_data.json()['errno'] =='0':
                    tocken = self.toc_base(data[self.telephone][0])
                    roomid = data[self.telephone][1]
                elif req_data.json()['errno'] == '100002':
                    log_in=self.again_log()
                    tocken = self.toc_base(log_in[0])
                    roomid = log_in[1]
                    data[self.telephone] = log_in
                    read_txt.DoTxt('../data/log_tocken.txt').write_txt(str(data))
                else:
                    print('接口报错了')
            else:
                re_tocken=self.again_log()
                tocken=self.toc_base(re_tocken[0])
                roomid=re_tocken[1]
                data[self.telephone]=re_tocken
                read_txt.DoTxt('../data/log_tocken.txt').write_txt(str(data))
            return [tocken,roomid]


if __name__ == '__main__':
    a= ForTocken('18600000005').return_tocken()
    print (a)