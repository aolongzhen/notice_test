from hashlib import md5
import time


class CreateSign():
    global sign_time
    def create_sign(self,param,secret_key):
        global sign_time
        sign_time=int(time.time())
        param_for_sign='&'.join(['{}={}'.format(k, v) for k, v in sorted(param.items())])
        sign=md5('{}|{}|{}'.format(param_for_sign, sign_time, secret_key).encode('utf-8')).hexdigest()



        return sign

if __name__ == '__main__':
    a = CreateSign().create_sign(param='telphone=18100000001',secret_key='d1b4235309a4e8aebcd6842fa7d842f5')
    print (a)



