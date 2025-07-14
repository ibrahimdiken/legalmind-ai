# 🧠 LegalMindAI

**LegalMindAI**, Türkçe dilinde çalışan yapay zekâ destekli bir hukuki danışmanlık aracıdır.  
OpenAI tabanlı güçlü bir LLM (Large Language Model) kullanarak, kullanıcıların hukuki sorularına akıllı, hızlı ve anlamlı yanıtlar verir.

> 🚀 Ayrıca proje Model Context Protocol (MCP) yapısıyla geliştirildi. Bu sayede geçmiş sorgular loglanabilir ve dış sistemlerle entegrasyon yapılabilir.

---

## 🎯 Özellikler

- ✅ **LLM Tabanlı Hukuki Danışmanlık:** Doğal dilde yazılmış sorulara detaylı yanıt verir.
- 🔗 **MCP API Endpoint:** JSON tabanlı API üzerinden dış sistemler sorgu gönderebilir.
- 💾 **Geçmiş Sorguların Loglanması:** Tüm MCP istekleri `logs/mcp_history.json` dosyasında kayıt altına alınır.
- 🌐 **Basit ve Anlaşılır Web Arayüzü:** Flask ile geliştirilmiş frontend (HTML + CSS).
- 📂 **Geçmiş Kayıtları Görüntüleme & İndirme:** Yapılan sorgular `history` sayfasında listelenebilir, JSON olarak indirilebilir.

---

## 🚀 Kurulum

### 1. Projeyi klonla

```bash
git clone https://github.com/ibrahimdiken/legalmind-ai.git
cd legalmind-ai
```
---
### 2. Virtual environment oluştur ve aktif et
```bash
python3 -m venv venv
source venv/bin/activate
```
---

### 3. Gerekli bağımlılıkları yükle
```bash
pip install -r requirements.txt
```


### 4. .env dosyasını oluştur
Ana dizine .env adlı bir dosya oluşturun ve içine OpenAI API anahtarınızı girin:

```bash
OPENAI_API_KEY=sk-xxx

```
### 🧪 Uygulamayı Çalıştır

```bash
python3 run.py

```
Tarayıcıdan aç: http://localhost:5500















