from common import http_requests,for_api_tocken
from conf import  project_path

#前提条件，调用登录类，使用手机号登录（手机号写死）
#第一步验证提醒灯接口，接口返回大于0，则通过
#第二部验证通知接口，通知中能找到添加的对应的通知ID，则通过

class CheckPoint():

    def __init__(self,notice_id,send_time,tocken):
        self.notice_id=notice_id
        self.send_time=send_time
        self.tocken=tocken



    def verify_result(self):
        #请求提醒灯接口 验证noticeNum大于0
        url='https://new-test-ck.haochang.tv/api/user/notification'
        headers={'x-api-test': 'true','authorize-token': self.tocken,'app-version': '1.7.0'}
        notification= http_requests.RequestsClass(url=url, param={"lastNotifyTime":self.send_time}, headers=headers).http_requests(method='get')
        msg='提醒灯数量:'+notification.json()['data']['noticeNum']
        if eval(notification.json()['data']['noticeNum']) ==0:
            print (msg,'通知提醒灯错误')
        elif eval(notification.json()['data']['noticeNum']) >0 :
            print (msg,'通知提醒灯测试通过')
        else:
            print (notification,'程序错误')


        #请求通知接口 验证通知下发
        url='https://new-test-ck.haochang.tv/api/notice'
        notice= http_requests.RequestsClass(url=url, param={"lastNotifyTime":str(self.send_time)}, headers=headers).http_requests(method='get')
        print(notice.json())
        notices=notice.json()['data']['list']
        for i in notices:
            if i['noticeId'] == str(self.notice_id):
                notice = self.notice_id

                print('系统通知测试通过')
                break
        if notice is notice != self.notice_id:
            print ('系统通知测试不通过')


if __name__ == '__main__':
    tocken=for_api_tocken.ForTocken('18600000000').return_tocken()
    a = CheckPoint(notice_id='676565',send_time='',tocken=tocken[0]).verify_result()