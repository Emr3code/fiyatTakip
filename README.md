# 🛒 E-Ticaret Fiyat Takip Botu (Price Tracker)

Bu proje, belirlenen e-ticaret ürünlerini (Trendyol, Hepsiburada, Amazon vb.) 7/24 otomatik olarak izleyen ve fiyat değişikliği/indirim durumunda kullanıcıya **Telegram** üzerinden anlık bildirim gönderen bir Python otomasyonudur.

## Proje Görseli
<img width="1904" height="1026" alt="image" src="https://github.com/user-attachments/assets/c774b040-3e57-4eb2-ad47-0889ab156b46" />
<img width="486" height="241" alt="image" src="https://github.com/user-attachments/assets/4651feae-ad4a-4c06-912d-3068f34d50a0" />


*(Buraya aldığın ekran görüntüsünü ekleyebilirsin)*

## 🚀 Özellikler

* **Anlık Takip:** Belirlenen periyotlarla (örneğin 60 saniyede bir) ürün sayfasını tarar.
* **Anti-Bot Koruması:** `undetected-chromedriver` kütüphanesi sayesinde Cloudflare ve bot korumalarına takılmadan çalışır.
* **Telegram Bildirimi:** Fiyat bilgisini ve ürün linkini doğrudan cebinize mesaj olarak atar.
* **Arkaplan Çalışma:** Sistem tepsisinde veya arka planda sessizce çalışabilir.

## 🛠️ Kullanılan Teknolojiler

* [Python 3.x](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [Undetected Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
* Telegram Bot API

## ⚙️ Kurulum ve Kullanım

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1.  **Repoyu Klonlayın:**
    ```bash
    git clone [https://github.com/kullaniciadi/fiyat-takip-botu.git](https://github.com/kullaniciadi/fiyat-takip-botu.git)
    cd fiyat-takip-botu
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    # Veya manuel olarak:
    pip install selenium undetected-chromedriver requests
    ```

3.  **Ayarları Yapın:**
    `main.py` dosyası içerisindeki şu alanları kendi bilgilerinizle doldurun:
    * `BOT_TOKEN`: BotFather'dan alınan Telegram Tokeni.
    * `CHAT_ID`: Mesajın gideceği Telegram ID'si.
    * `URUN_LINKI`: Takip etmek istediğiniz ürünün linki.

4.  **Çalıştırın:**
    ```bash
    python main.py
    ```

## ⚠️ Yasal Uyarı
Bu proje eğitim ve kişisel kullanım amaçlı geliştirilmiştir. Web sitelerinin kullanım koşullarına (ToS) saygı gösterilmelidir. Çok sık istek göndermek IP adresinizin engellenmesine neden olabilir.

---
**Geliştirici:** Emr3Code
