from test_case import  sys_notice_test
from common import  for_api_tocken,do_redis
import check_point

#生成系统通知
sys_notice_test

#删除redis缓存
#do_redis.DoRedis('user:notification:11373864',0).updata_key()

#执行测试点
#tocken=for_api_tocken.ForTocken('18600000000').return_tocken()
#check_point.CheckPoint(sys_notice_test.notice_id,sys_notice_test.t,tocken[0]).verify_result()
