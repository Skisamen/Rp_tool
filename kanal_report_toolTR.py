import requests
from fake_useragent import UserAgent
from faker import Faker
import os
import marshal
import base64




banner = """
  _______   _                                
 |__   __| | |                               
    | | ___| | ___  __ _ _ __ __ _ _ __ ___  
    | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \ 
    | |  __/ |  __/ (_| | | | (_| | | | | | |
    |_|\___|_|\___|\__, |_|  \__,_|_| |_| |_|
                    __/ |                    
                   |___/                     

@toolturkish

Selamın Aleyküm. Bu tool İnovapin ailesi için yapılmıştır sadece kendi kullanıcı adını girerek bu tool a girebilirler.

İlk Başta Onlara Verdiğim Tool Şifresini Girecekler 

Sonra Onlara Verdiklerim Kullanıcı Adı ve Şifreyi girecekler

Daha Sonra Patlatmak istedikleri kanalın kullanıcı adını yazarak türkçe bir şekilde telegramın destek sitesine göndermede bulunacaktır
"""

print("\033[31m",banner,"\033[0m")

import os

try:
    # .PY_PRIVATE klasörünü oluşturma
    os.makedirs('.PY_PRIVATE/.alphaexploit', exist_ok=True)

    # Tool şifresi
    tool_password = "inovapin"

    # Kullanıcı adı ve şifre listesi
    users = {
        "@SucsuzBey": "faşist1",
        "@emirrdaily": "Emir1",
        "@againtr": "Alpha1",
        "@Itaatediceksinizz": "Yucen1z1",
        "@YuceSenic": "Senic1",
        "@suclubey": "Flawsome1",
        "@Z1wortex": "@wortex91",
        "@Kawixx15": "Kamraan1",
        "@LyroxYeniden": "Lyrox1", 
        "@ati": "ati2421", 
        "@Pandispanya26": "panda1", 
    }

    # Tool şifresini kontrol etme
    tool_input = input("Tool şifresini girin: ")
    if tool_input != tool_password:
        print("Hatalı tool şifresi! Çıkılıyor...")
        exit()

    print("Tool'a giriş başarılı!")

    # Kullanıcı giriş bilgilerini alma
    username = input("Kullanıcı adınızı girin (örn: @inovapin) : ")
    password = input("Şifrenizi girin : ")

    # Kullanıcı doğrulama
    if username in users and users[username] == password:
        print(f"Hoş geldin {username}! Giriş başarılı.")
    else:
        print("Hatalı kullanıcı adı veya şifre!")
        exit()

except Exception as e:
    print(f"Hata oluştu: {e}")



target_user = input("Kanalın Kullanıcı Adını Girin :")

fake = Faker()

text = f"""Telegram'da fuhuş ve pornografi gönderen ve bir Telegram şirketinin sahibi olduğunu söyleyen bir kişiyi sizlere bildiriyoruz. Siz değerli takipçilerimizin işgalci kimliğini çekmemeleri için yardımcı olmanızı ve kişinin hesabını durdurmanızı rica ediyoruz. Bu kanalların durdurulmasını diliyoruz. Teşekkürler Telegram Ekibi

Çocuk Pornosu atan Kanal : {target_user}
"""



def report():
    username = fake.user_name()
    domain = fake.free_email_domain()
    email = f"{username}@{domain}"

    country_code = fake.country_calling_code()
    mobile_number = fake.random_number(digits=10)
    generated_number = f"{country_code}{mobile_number}"

    
    user_agent = UserAgent().random

    cookies = {
        'stel_ssid': '5a60a4bb956e6b097e_10199437230854365722',
    }

    headers = {
        'authority': 'telegram.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    data = {
        'message': text,
        'legal_name': target_user,
        'email': email,
        'phone': generated_number,
        'setln': 'tr',
    }

    try:
        response = requests.post('https://telegram.org/support', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()

        if response.status_code == 200 and '<div class="alert alert-success">' in (response.text):
            print(response ,f" \033[32m{email} : Report done !!\033[0m")
        else:
            print(response,"\033[31mReport Failed.\033[0m")
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

while True:
    report()


