import configparser

class ReadConfig:

    def __init__(self, filepath):
        self.cf =configparser.ConfigParser()
        self.cf.read(filepath,encoding='UTF-8')

    def read_config(self,section,option):
        value=self.cf.get(section,option)
        return value


if __name__ == '__main__':
    a = ReadConfig(filepath='config/log_config.conf').read_config(section='CONFIG',option='state')
    print (a)