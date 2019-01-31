class DoTxt:
    def __init__(self,path):
        self.path=path


    def read_txt(self):
        file=open(self.path)
        data=file.read()
        file.close()
        return data


    def write_txt(self,write_data):
        file =open(self.path,'r+')
        file.write(write_data)
        file.close()

if __name__ == '__main__':
    a = DoTxt('log_tocken.txt').read_txt()
    print (a)