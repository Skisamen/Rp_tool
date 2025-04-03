import requests
from fake_useragent import UserAgent
from faker import Faker
import random

# Proxy listesini dosyadan yükleme
def load_proxies(filename="proxies.txt"):
    try:
        with open(filename, "r") as file:
            proxies = [line.strip() for line in file.readlines() if line.strip()]
        return proxies
    except FileNotFoundError:
        print("Proxy dosyası bulunamadı! Lütfen 'proxies.txt' dosyanızı oluşturun.")
        exit()

# Proxy listesini yükle
proxy_list = load_proxies()

# Banner
banner = """
  _______   _                                
 |__   __| | |                               
    | | ___| | ___  __ _ _ __ __ _ _ __ ___  
    | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \ 
    | |  __/ |  __/ (_| | | | (_| | | | | | |
    |_|\___|_|\___|\__, |_|  \__,_|_| |_| |_|
                    __/ |                    
                   |___/                     

"""
print("\033[31m", banner, "\033[0m")

# Tool şifresi ve kullanıcı doğrulama
tool_password = "inovapin"
users = {"@againtr": "Alpha1"}

tool_input = input("Tool şifresini girin: ")
if tool_input != tool_password:
    print("Hatalı tool şifresi! Çıkılıyor...")
    exit()

username = input("Kullanıcı adınızı girin (örn: @inovapin) : ")
password = input("Şifrenizi girin : ")
if username in users and users[username] == password:
    print(f"Hoş geldin {username}! Giriş başarılı.")
else:
    print("Hatalı kullanıcı adı veya şifre!")
    exit()

# Kullanıcıdan hedef bilgilerini alma
target_user = input("Kullanıcı adı gir: ")
dil = input("Hangi dili seçeceksin (örn: ru, tr, en, ar): ")
fake = Faker()
text = input("Rapor mesajını gir: ")

# Rapor fonksiyonu
def report():
    username = fake.user_name()
    domain = fake.free_email_domain()
    email = f"{username}@{domain}"
    country_code = fake.country_calling_code()
    mobile_number = fake.random_number(digits=10)
    generated_number = f"{country_code}{mobile_number}"
    user_agent = UserAgent().random

    # Rastgele proxy seçme
    proxy = random.choice(proxy_list)
    proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"}

    cookies = {"stel_ssid": "5a60a4bb956e6b097e_10199437230854365722"}
    headers = {
        "authority": "telegram.org",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "user-agent": user_agent,
        "sec-fetch-site": "none",
    }

    data = {
        "message": text,
        "legal_name": target_user,
        "email": email,
        "phone": generated_number,
        "setln": dil,
    }

    try:
        response = requests.post("https://telegram.org/support", cookies=cookies, headers=headers, data=data, proxies=proxies, timeout=10)
        response.raise_for_status()

        if response.status_code == 200 and '<div class="alert alert-success">' in response.text:
            print(f"\033[32m{email} : Report done using {proxy}!\033[0m")
        else:
            print(f"\033[31mReport Failed using {proxy}.\033[0m")
    except requests.exceptions.RequestException as e:
        print(f"\033[31mProxy Error ({proxy}): {e}\033[0m")

# Sürekli çalıştır
while True:
    report()
