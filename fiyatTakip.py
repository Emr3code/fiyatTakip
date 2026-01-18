import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import requests

def telegrama_at(mesaj):
    # Buraya kendi chat id'ni tekrar yapıştır:
    chat_id = "xxx"
    # Buraya kendi tokenini tekrar yapıştır:
    bot_token = "xxx" 
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': mesaj}
    requests.post(url, data=payload)

def main():
    print("-> Fiyat Ajanı Başlatılıyor... 🕵️‍♂️")
    
    # 1. Hangi ürünü takip edelim? (Örnek: Bir iPhone kılıfı falan yapıştırabilirsin)
    # Buraya rastgele bir Trendyol linki koydum, istersen değiştir:
    urun_linki = "https://www.trendyol.com/lenovo/ideapad-slim-3-intel-core-i5-13420h-8gb-512ssd-15-3-wuxga-freedos-dizustu-bilgisayar-83k1004etr-p-929838698?boutiqueId=689770&merchantId=968"
    

    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, use_subprocess=True)
    driver.minimize_window() 
    
    print(f"-> Ürüne gidiliyor: {urun_linki}")
    driver.get(urun_linki)
    time.sleep(5)
    
    try:
        # Trendyol'da fiyat genelde bu class'ta olur, siteye göre değişir bu kısım
        fiyat_elementi = driver.find_element(By.CLASS_NAME, "price-container") 
        fiyat = fiyat_elementi.text
        
        print(f"✅ FİYAT ÇEKİLDİ: {fiyat}")
        telegrama_at(f"💰 Ürün Fiyatı: {fiyat}\nLink: {urun_linki}")
        
    except:
        print("❌ Fiyat bulunamadı (Class ismi değişmiş olabilir)")
    
    input("Kapatmak için Enter'a bas...")

if __name__ == "__main__":

    main()
