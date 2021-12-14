import os,win32api, shutil, subprocess,fnmatch 

class AdsSecurityRemover:
    def __init__(self):
        self.file_path_li = []
        self.ext_file_path = []
        self.adsfile = []
        self.get_alldrives = win32api.GetLogicalDriveStrings().split('\0')
     
    def providing_security(self): 
        try:
            for drive in self.get_alldrives:
                for root,subdir,files in os.walk(drive):
                    # self.find_ads(root)
                    for file in files:
                        filepath = os.path.join(root,file)
                        subprocess.Popen(f"powershell.exe Remove-Item {filepath} -Stream *",shell = True)
                
        except:
            pass
        
if __name__ == "__main__":
    obj = AdsSecurityRemover()
    obj.providing_security()