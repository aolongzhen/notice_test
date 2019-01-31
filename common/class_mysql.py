import mysql.connector  # 操作数据库

from  common.read_config import ReadConfig


class DomysqlData:
    #conifig：数据库连接配置、sql：sql语句、state：(1:查询，2：更新)
    def __init__(self,config ,state,sql,data):
        self.config=config
        self.sql=sql
        self.data=data
        self.state=state

    def read_data(self):
        #连接数据库
        cnn = mysql.connector.connect(**eval(self.config))

        # 游标-->cursor --> 获取操作数据库的权限
        cursor = cnn.cursor()

        #判断是查询还是更新
        if self.state == 1:
            cursor.execute(self.sql,self.data)
            result = cursor.fetchall()
        elif self.state == 2:
            cursor.execute(self.sql, self.data)
            cursor.execute('commit')
            result=[]

        #关闭游标
        cursor.close()

        #关闭连接
        cnn.close()
        return result



if __name__ == '__main__':
    config = ReadConfig(filepath='db_con.conf').read_config(section='DATABASE', option='config')
    data = ('name1548752429923',)
    sql = 'select mic_task_id from activity_room_mic_task where name= %s'

    result = DomysqlData(config=config, sql=sql, state=1,data=data).read_data()
    print (result)