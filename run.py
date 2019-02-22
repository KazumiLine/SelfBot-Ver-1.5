# -*-coding: utf-8 -*-
import os,sys,time,platform
def CleanMSG():
    if "Windows" in platform.platform():
            _ = os.system("cls")
    else:
        _ = os.system("clear")
print("以下為系統登入選項\n 1.既存token\n 2.網址登入\n 3.輸入token\n 4.LINE帳密")
way = str( input("[※]請選擇汝欲登入的方式 :"))
if way =='1':
    f = open('bot/token.txt','r')
    ttoken = f.read()
    f.close()
elif way =='2':
    ttoken = ""
elif way =='3':
    ttoken = str( input('請輸入Token:'))
elif way =='4':
    print("請輸入您的帳號及密碼")
    ttoken = str( input('Email: ')) + ", "
    while 1:
        psw = str( input('Password: '))
        if psw.replace(" ","") == "":
            print("警告！您輸入的密碼為\"空白\"，請重新輸入...")
        else:
            ttoken += psw
            break
else:
    print("您輸入並非上述選項，程式將自動關閉")
    sys.exit()
t = open('bot/run.txt','w')
t.write(ttoken)
t.close()
print("登入中....如果您非使用紀錄過的token登入，系統將紀錄最新token")
CleanMSG()
os.system("python3 bot/x.py")
