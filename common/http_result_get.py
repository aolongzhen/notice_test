#用来提取配置的接口返回，获取实际结果的路径
import sys
from common import  class_log
import time


class ResultValue():
    def __init__(self,result_json,except_result_conf): #result_json接口返回json，except_result_conf需要验证接口返回值结构路径，例如：'one.two1.three1'
        self.result_json=result_json
        self.except_result_conf=except_result_conf


    def return_value(self):
        erclist=self.except_result_conf.split('.')
        t = time.strftime('%Y.%m.%d',time.localtime(time.time()))

        for i in range(0,len(erclist)-1): #循环取最后一层dict
            if erclist[i] in self.result_json:
                self.result_json = self.result_json[erclist[i]]
            else:
                class_log.Mylog(str(t) + 'syserr.txt').debug(msg=erclist[i] + "参数错误，key不存在", Handler=2)
                sys.exit(0)
          #从最后一层dict中取值，因为上次层循环直接取最后一个值报错 所有这么处理
        if erclist[len(erclist)-1] in self.result_json:
            result_value =self.result_json[erclist[len(erclist)-1]]
        else:
            class_log.Mylog(str(t)+'SYSERR.txt').debug(msg=erclist[i] + "参数错误，key不存在", Handler=2)
            sys.exit(0)

        return result_value

if __name__ == '__main__':
    ResultValue({"one":{"two":{"three":"value"}}},'one.two.thr1e').return_value()





