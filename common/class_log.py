#日志系统
import logging

from common import project_path
from common.read_config import ReadConfig


class Mylog:
    #获取配置文件路径
    logconfig_path= project_path.log_path


    #获取配置log配置信息
    readconfig = ReadConfig(logconfig_path)
    format= readconfig.read_config(section='CONFIG', option='formatter')
    conf_level= readconfig.read_config(section='CONFIG', option='level')


    #获取生成日志报告目录
    test_report_path= project_path.test_report_path

    # msg_level：容器log级别 level:日志输出级别 Handler:输出渠道1：控制台 2：文件 3：控制台和文件都有
    def my_log(self,msg,msg_level,Handler,log_name='auto_cases',level= conf_level,log_file_path='test_log.txt',format=format):
        #创建日志容器
        logger=logging.Logger(log_name,msg_level)

        # 定义格式
        formatter = logging.Formatter(format)
        # 判断输出哪个渠道 相对路径（fh：文件输出，sh：控制台输出）
        if Handler == 1:
            sh = logging.StreamHandler()
            sh.setLevel(level)
            logger.addHandler(sh)
            sh.setFormatter(formatter)

        elif Handler == 2:
            fh = logging.FileHandler(log_file_path, encoding='UTF-8')
            fh.setLevel(level)
            logger.addHandler(fh)
            fh.setFormatter(formatter)


        elif Handler == 3:
            fh = logging.FileHandler(log_file_path, encoding='UTF-8')
            sh = logging.StreamHandler()

            # 渠道输出级别
            fh.setLevel(level)
            sh.setLevel(level)

            # 输出渠道添加到logger
            logger.addHandler(fh)
            logger.addHandler(sh)

            # 格式化输出内容
            fh.setFormatter(formatter)
            sh.setFormatter(formatter)

        if msg_level == 'DEBUG':
            logger.debug(msg)
        elif msg_level == 'INFO':
            logger.info(msg)
        elif msg_level == 'WARNING':
            logger.warning(msg)
        elif msg_level == 'ERROR':
            logger.error(msg)
        elif msg_level == 'CRITICAL':
            logger.critical(msg)

        logger.removeHandler(fh)

        #移除渠道
        if Handler == 2:
            logger.removeHandler(fh)
        elif Handler == 1:
            logger.removeFilter(sh)
        elif Handler == 3:
            logger.removeHandler(fh)
            logger.removeFilter(sh)



    def debug(self,msg,Handler):
        self.my_log(msg,msg_level='DEBUG',Handler=Handler)
    def info(self,msg,Handler):
        self.my_log(msg,msg_level='INFO',Handler=Handler)
    def error(self,msg,Handler):
        self.my_log(msg,msg_level='ERROR',Handler=Handler)
    def warning(self,msg,Handler):
        self.my_log(msg,msg_level='WARNING',Handler=Handler)
    def critical(self,msg,Handler):
        self.my_log(msg,msg_level='CRITICAL',Handler=Handler)


if __name__ == '__main__':
        Mylog().debug(msg="aaaaaaaaaaaaaaaaaaaaaaaaaa",Handler=2)