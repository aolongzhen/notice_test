import redis

class DoRedis:
    pool = redis.ConnectionPool(host='192.168.1.24',port=6379,password='',db=1,decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    def __init__(self,key,value=None):
        self.key=key
        self.value=value

    def updata_key(self):
        self.r.set(self.key, self.value, ex=None, px=None, nx=False, xx=False)


    def del_key(self):
        self.r.delete(self.key)


if __name__ == '__main__':
    DoRedis(key='sys:notice:id:generator').del_key()



