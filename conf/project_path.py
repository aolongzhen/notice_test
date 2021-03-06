import os

from common.read_config import ReadConfig

project_conf_path=os.path.split(os.path.realpath(__file__))[0]+'\\file_path.conf'
project_path=ReadConfig(filepath=project_conf_path).read_config(section='PROJECT_PATH',option='project')

#headers配置文件路径
headers_path = os.path.join(project_path,'conf','request_headers.conf')

#db配置文件路径
db_path = os.path.join(project_path,'conf','db_con.conf')

#email配置文件路径
email_path = os.path.join(project_path,'conf','email.conf')

#HTTP配置文件路径
http_path = os.path.join(project_path,'conf','http.conf')

#log配置文件路径
log_path = os.path.join(project_path,'conf','log_config.conf')

#sign配置文件路径
sign_path = os.path.join(project_path,'conf','sign.conf')
#test_report_path文件夹路径
test_report_path = os.path.join(project_path,'report')

#logfile文件夹路径
log_file = os.path.join(project_path,'report')


#notice 配置文件

notice_file=os.path.join(project_path,'conf','notice.conf')

#执行日志文件

test_log=os.path.join(project_path,'test_case','test_log.txt')

#登录数据文件

log_data=os.path.join(project_path,'data','log_tocken.txt')


#redis配置文件路径
redis_conf=os.path.join(project_path,'conf','redis.conf')


#系统日志
sys_log = os.path.join(project_path,'log\\')

if __name__ == '__main__':
    print (os.path.split(os.path.realpath(__file__))[0])