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
        url = 'http://new-test.ck.haochang.tv/admin/notices/system/edit'
        param = {"title":"title","intro":"intro","content":"content","display_in_con":0,"display_in_list":0,"type_id":1,"picture_url":"","publish_time":""}
        headers = {"cookie":"PHPSESSID=aggkm4rhdn9club9d97c964nb7","X-HTTP-Method-Override":"POST","Referer": "http://new-test.ck.haochang.tv/admin/notices/system/edit"}
        a = RequestsClass(url=url, param=param, headers=headers).http_requests(method='post')
        print(a)


