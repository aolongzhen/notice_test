from common import http_requests,for_api_tocken,class_log,http_result_get
import time


#前提条件，调用登录类，使用手机号登录（手机号写死）
#第一步验证提醒灯接口，接口返回大于0，则通过
#第二部验证通知接口，通知中能找到添加的对应的通知ID，则通过

class CheckPoint():

    def __init__(self,notice_id,send_time,tocken):
        self.notice_id=notice_id
        self.send_time=send_time
        self.tocken=tocken
        self.t = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    def verify_result(self):
        #请求提醒灯接口 验证noticeNum大于0
        url='https://new-test-ck.haochang.tv/api/user/notification'
        headers={'x-api-test': 'true','authorize-token': self.tocken,'app-version': '1.7.0'}
        notification= http_requests.RequestsClass(url=url, param={"lastNotifyTime":self.send_time}, headers=headers).http_requests(method='get')
        noticeNum=http_result_get.ResultValue(notification.json(),'data.noticeNum').return_value()
        class_log.Mylog(self.t+'test.txt').debug(msg="提醒灯数量："+noticeNum, Handler=2)
        if eval(noticeNum) ==0:
            class_log.Mylog(self.t + 'test.txt').debug(msg="通知提醒灯错误" + noticeNum, Handler=2)
            class_log.Mylog(self.t + 'testerr.txt').debug(msg="通知提醒灯错误" + noticeNum, Handler=2)
        elif eval(noticeNum) >0 :
            class_log.Mylog(self.t + 'test.txt').debug(msg="通知提醒灯测试通过：" + noticeNum, Handler=2)
        else:
            class_log.Mylog(self.t + 'testerr.txt').debug(msg="程序错误" , Handler=2)


        #请求通知接口 验证通知下发
        url='https://new-test-ck.haochang.tv/api/notice'
        notice= http_requests.RequestsClass(url=url, param={"lastNotifyTime":str(self.send_time)}, headers=headers).http_requests(method='get')
        notices= http_result_get.ResultValue(notice.json(), 'data.list').return_value()
        result_notice_list = []
        for i in notices:
            result_notice_list.append(i['noticeId'])
        if self.notice_id in result_notice_list:
            class_log.Mylog(self.t + 'test.txt').debug(msg="通知列表测试通过：" + self.notice_id, Handler=2)
        else:
            class_log.Mylog(self.t + 'test.txt').debug(msg="通知列表测试不通过：" + self.notice_id, Handler=2)
            class_log.Mylog(self.t + 'testerr.txt').debug(msg="通知列表测试不通过"+ self.notice_id+'不存在', Handler=2)


if __name__ == '__main__':
    tocken=for_api_tocken.ForTocken('18600000000').return_tocken()
    a = CheckPoint(notice_id='676588',send_time='',tocken=tocken[0]).verify_result()