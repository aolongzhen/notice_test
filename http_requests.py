import requests
class RequestsClass():
    def __init__(self,url,param,headers='None'):
        self.url=url
        self.param=param
        self.headers=headers


    def http_requests(self,method):
        if method== 'get':
            result= requests.get(self.url,self.param,headers=self.headers,timeout=20)

        elif method == 'post':
            result= requests.post(self.url, self.param,headers=self.headers,timeout=20)

        elif method == 'put':
            result = requests.put(self.url, self.param, headers=self.headers, timeout=20)
        return result


#如下是测试代码
if __name__ == '__main__':
        url = 'http://test-audio-book-admin.haochang.tv/admin/statistics'
        param = {"date":"20190114"}
        headers = {"authorize-token": "7|1546836421|6d2c246a0f9864511427bad2a2daa253",
                   "Origin": "http://test-audio-book-admin.haochang.tv",
                   "Referer": "http://test-audio-book-admin.haochang.tv",
                   "X - Requested - With": "XMLHttpRequest"}
        a = RequestsClass(url=url, param=param, headers=headers).http_requests(method='get')
        print(a)


