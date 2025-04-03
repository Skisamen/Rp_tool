

import lzma
import zlib
import codecs
import base64
import os
os.system("pip install pyfiglet")
os.system("pip install requests")
os.system('pip install webbrowser')
os.system('pip install user_agent')
os.system('clear')
import requests,random,pyfiglet,webbrowser,sys,time
from random import randint
from user_agent import generate_user_agent as ua
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("tg report")
print(a_bSa+ab)
def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

to(
    f"\033[31;m TOOL >> \033[1;36mTELEGRAM REPORT SCRIPT\n\033[1;31m DEVELOPER >>\033[1;33m @toolturkish \n\033[31;m JOIN >> \033[1;36m @inovapin  \n")
def R(m,email,num):
 res=requests.get('https://telegram.org/support',headers={"Host": "telegram.org","cache-control": "max-age\u003d0","sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","user-agent":ua(),"accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "cross-site","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://www.google.com/","accept-encoding": "gzip, deflate, br, zstd","accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"}).cookies;stel=res['stel_ssid'];data=f'message={m}&email={email}&phone={num}&setln=';req=requests.post('https://telegram.org/support',data=data,headers={"Host": "telegram.org","cache-control": "max-age\u003d0","sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://telegram.org","content-type": "application/x-www-form-urlencoded","user-agent":ua(),"accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://telegram.org/support","accept-encoding": "gzip, deflate, br, zstd","accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5","cookie":f"stel_ssid={stel}"}).text;print();#print((req.split('class="alert alert-success"><b>')[1].split('<')[0]))
 
 if "Thanks" in req:
  
  
  print(f'{G}[√]REPORT{E}==>{B} SUCCESS {E}| {G}{E}{B} {G}FROM{E}==> \033[35;m{email}{B} \nTHIS TOOL IS @toolturkish\n')
 else:
  print("Error Report")
u=input(
"\033[30;m[×] Enter Username of scammer : "
)
m = """Merhaba telegram

Bir kişi hakkında bir rapor yapacağım ve bu kişi bir yalancı"""+u+"""o bir dolandırıcı, telgrafta olmaması gerekiyor, birçok insan şikayet ediyor ama kimse konuşmuyor çünkü uğraşmaya değmez. Ancak, bununla ilgileneceğim, lütfen yardım edin. BU BIR IHBAR MESAJIDIR. BUNU YETKILILERE DUYURUYORUM. Teşekkürler


"""

names = ["raof","alpha","usamaan","fazel","aymen","abdulmalek","moneyman911","mohammed","Naseer","Whis","REEKY.","spamkiller","des.175","deveing","meraff","viratkohli","spammers","hackers","pleesa","3nefa_iraq","pagesouls","erycka","jessy","lola","mentezer","frhon","jasim","karrar","radwan","haider","zainab","ahmed","alivelibaba","youssef"]

while True:
 num="+91",randint(9392823620,9994997058)
 email = f'{random.choice(names)}{randint(9392820,9994958)}@gmail.com'
 
 
 R(m,email,num)
#Dec bY JOKER: @Theyhates_joker  oN: @JokerToolzz 🔥❄. 

