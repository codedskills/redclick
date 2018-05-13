'''
    CODEDSKILLS INC,.
    THIS IS REDCLICK.PY A RESOURCE DOWNLOADER FRAMWORK
    for Linux Written in python
    Download the latest update here!!
'''









from time import sleep
from sys import stdout, exit
from os import system, path
import multiprocessing
from urllib import urlopen
from platform import system as systemos, architecture
from wget import download
from argparse import ArgumentParser
import os
import sys


RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'

def connected(host='http://www.duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False

if connected() == False:
    print('''

{0}||||___________________________||||
!!!!        Error 69!!         !!!!
!!!!     NIGGA GOT NO CHILL    !!!!
!!!!           XDDDD           !!!!
||||___________________________||||{1}


        {0}[Error]{1} OOps Not Connected To Internet :-(''').format(RED,END)
    exit(0)

def checkOS():
    ostype = systemos().lower()
    if (ostype == "linux"):
        return True
    else:
        print('''
        {0}
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
             OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOOOOOOOOOOOOOOOOOO
                    OOOOOOOOOOOOOOOOOO
                        [[[[[]]]]]
                        ^^^^^^^^^^
                        <><><><><>{1}


                        GROW UP!!!
                        START USING LINUX
                    {0}https://www.kali.org/downloads{1}

        ''').format(END,GREEN)

        return False
        exit(0)

HOST_URL = "http://google.com/hosted/webpage_uri/"

def downloadReq():
     args = ArgumentParser()
     args.add_argument('-install',dest='install_code', help='Packages Name')
     args.add_argument('-v' ,dest='version_code', help='Version of Package(Optional)')
     args.add_argument('-update',dest='update_virtual',help='Update The Redclick`s Script' )
     args = args.parse_args()
     if not args.install_code:
         if args.update_virtual:
            updateSys()
            exit()
         else:
             print("Missing Argument : No package specified")

     if not args.version_code:
         print("No version selected>>{0}Custom Mode").format(GREEN)
         downloadReqNoVer(pkg=args.install_code)
         exit()
     filename = args.install_code
     file_ver = args.version_code
     fileurl = "http://exploitable-web.ml/shared/"+filename+"/"+file_ver+"/"+filename+".zip"
     print("Fetching"+filename+"from " +fileurl)
     download(fileurl)
     print('Westing Zone')
     print("Extracting Packages")
     system('unzip ' + filename+'.zip -d www/')
     system('rm -Rf '+filename+'.zip')
     system('figlet success!!')
     exit('SuccesFully Downloaded')

def updateSys():
    tempFolder = "tempCa"
    print("Backing Up Libraries")
    system('mkdir tempCa')
    system('cp -r www tempCa/')
    print("Getting Updates From Server")
    download('http://exploitable-web.ml/shared/redclick.new.zip')
    system('unzip redclick.new.zip')
    print("Checking Status")
    print("Configuring Folder")
    system('cp -r redclick.new/ /')
    system('rm -Rf redclick.new/')
    system('rm -Rf redclick.new.zip')
    system('cp -r tempCa/www /')
    system('rm -Rf tempCa/')
    print("Configured!!")

    system('figlet Updated SuccesFully')

def downloadReqNoVer(pkg):
    print("Connecting server :: {0}For{1} "+pkg).format(RED,END)
    fileurl = "http://exploitable-web.ml/shared/"+pkg+"/shared/"+pkg+'.zip'
    print("Fetching from " +fileurl)
    download(fileurl)
    print('Westing Zone')
    print("Extracting Packages")
    system('unzip '+pkg+'.zip -d www/')
    system('rm -Rf '+pkg+'.zip')
    system('figlet success!!')
    exit('SuccesFully Downloaded')


if __name__ == "__main__":
    try:
        checkOS()
        downloadReq()
    except KeyboardInterrupt:
        system('pkill -f python')
        exit()
