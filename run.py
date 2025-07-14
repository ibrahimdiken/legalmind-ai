#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from app import create_app

# .env’deki ayarlamaları yükle
load_dotenv()

app = create_app()

if __name__ == "__main__":
    print("🔧 LegalMindAI sunucusu port 5500’de başlatılıyor…")
    # host="0.0.0.0" ile dış IP’den de erişilebilir olur
    app.run(debug=True, host="0.0.0.0", port=5500)
