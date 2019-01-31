import os

from common.read_config import ReadConfig

project_conf_path=os.path.split(os.path.realpath(__file__))[0]+'\\file_path.conf'
project_path=ReadConfig(filepath=project_conf_path).read_config(section='PROJECT_PATH',option='project')

#headers配置文件路径
headers_path = os.path.join(project_path,'config','request_headers.conf')

#db配置文件路径
db_path = os.path.join(project_path,'config','db_con.conf')

#email配置文件路径
email_path = os.path.join(project_path,'config','email.conf')

#HTTP配置文件路径
http_path = os.path.join(project_path,'config','http.conf')

#log配置文件路径
log_path = os.path.join(project_path,'config','log_config.conf')

#sign配置文件路径
sign_path = os.path.join(project_path,'config','sign.conf')
#test_report_path文件夹路径
test_report_path = os.path.join(project_path,'report')

#logfile文件夹路径
log_file = os.path.join(project_path,'report')



if __name__ == '__main__':

    print (log_data_path,db_path,email_path,http_path,log_path,sign_path,log_file)
