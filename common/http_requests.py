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
        headers = {'x-api-test': 'true', 'authorize-token': 'MTE0OTY4MDcsMTU0ODkyOTQwNyw4NDFmMmQ4MWQzMjViOWUyODg1NzQ1MmZiNjhmZWMzNQ==', 'app-version': '1.7.0'}
        url = 'https://new-test-ck.haochang.tv/api/notice'
        notice = RequestsClass(url=url, param={"lastNotifyTime": str('1548996335000')},
                                             headers=headers).http_requests(method='get')
        print (notice.json())
