import redis
from conf import  project_path
from common import  read_config

class DoRedis:
    redis_conf_path=project_path.redis_conf
    read_redis=read_config.ReadConfig(filepath=redis_conf_path)
    host=read_redis.read_config(section='PARTY_NEW',option='host')
    post=read_redis.read_config(section='PARTY_NEW',option='port')
    password=read_redis.read_config(section='PARTY_NEW',option='password')
    db=read_redis.read_config(section='PARTY_NEW',option='db')
    decode_responses=read_redis.read_config(section='PARTY_NEW',option='decode_responses')
    pool = redis.ConnectionPool(host=host,port=eval(post),password=password,db=eval(db),decode_responses=decode_responses)
    r = redis.Redis(connection_pool=pool)
    def __init__(self,key,value=None):
        self.key=key
        self.value=value

    def updata_key(self):
        self.r.set(self.key, self.value, ex=None, px=None, nx=False, xx=False)


    def del_key(self):
        self.r.delete(self.key)


if __name__ == '__main__':
    DoRedis(key='user:notification:11373864').del_key()



