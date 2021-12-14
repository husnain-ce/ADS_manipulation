import os,win32api, shutil, subprocess,fnmatch 


"""
Captures the directory and than it will send it to find the ads filesystem
when it finds the file than it will return the file that is available in the form of list
and it returns 

After capturing the file list from you should have to remove that files 
Now you should have to check that the command from ads manipultion blogs in order to remove all
files    

"""


class AdsSecurity:
    def __init__(self):
        self.file_path_li = []
        self.ext_file_path = []
        self.adsfile = []
        self.get_alldrives = win32api.GetLogicalDriveStrings().split('\0')
     
    def providing_security(self): 
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
                    
    def find_ads(self,dir_under_process):
        cmd = subprocess.Popen(f"dir /r {dir_under_process}",stdout = subprocess.PIPE,stdin = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
        output_bytes = cmd.stdout.read() + cmd.stderr.read() 
        output_str = output_bytes.decode("utf-8", errors="replace")
        li = output_str.split()
        for file in li:
            if file.endswith(":$DATA"):
                self.adsfile.append(file)  
                
    def remove_ads_file(self):
        for i in self.adsfile:
            os.remove(i)