import glob
import os,subprocess
import time

def check_packages_and_install(polling_time):
    #os.chdir("c:\\PythonPrograms\\SessionLogs\\Package")

    tap_packages=glob.glob("*.TapPackage")
    for _ in tap_packages:
        print(_)
    os.chdir("C:\\Program Files\\Keysight\\Test Automation\\")
    #os.kill("Editor.exe")
    for _ in tap_packages:
        print("tap package install  \"c:\\Users\\Administrator\\opentap-Package\\"+ _ +"-f")
        subprocess.call(["tap package install","c:\\Users\\Administrator\\opentap-Package\\"+ _ +" -f"])
        #os.system("tap package install  \"c:\\Users\\Administrator\\opentap-Package\\"+ _ +"-f")

        time.sleep(200)

check_packages_and_install(1800)
#time.sleep(polling_time)