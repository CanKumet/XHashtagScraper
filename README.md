# 🧠 XHashtagScraper

**XHashtagScraper**, Python ve Selenium kullanarak [X.com](https://x.com) (eski adıyla Twitter) üzerinde belirli bir **hashtag** ile yapılan aramaları otomatikleştirir. Giriş yaptıktan sonra sonuçlardaki tweet'leri toplar ve terminale yazdırmanın yanı sıra bir `.txt` dosyasına da kaydeder.

## 🚀 Özellikler

- 🔐 X (Twitter) hesabı ile otomatik giriş
- 🔎 İstenilen hashtag'e göre tweet araması
- 🧹 Sayfada otomatik kaydırma ile daha fazla sonuç çekme
- 📝 Tweet metinlerinin temiz bir şekilde `tweetler.txt` dosyasına kaydedilmesi

## 📁 Çıktı

Tüm çekilen tweet'ler proje dizininde `tweetler.txt` adlı dosyaya şu şekilde yazılır:


## ⚙️ Gereksinimler

- Python 3.7+
- Google Chrome
- Uyumlu bir `chromedriver.exe`

Aşağıdaki Python kütüphanesi yüklenmelidir:

```bash
pip install selenium
git clone https://github.com/cankumet/XHashtagScraper.git
cd XHashtagScraper
