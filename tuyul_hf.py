import requests
import time
import os
from datetime import datetime

# --- CONFIGURATION ---
# Ambil URL dari environment variable, kalau ga ada pake default link Space Mas
TARGET_URL = os.getenv("TARGET_URL", "https://hadipramono05-test-ai.hf.space/")

# Identitas penyamaran biar dikira Chrome asli di Windows (Manusia)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

def ketuk_pintu():
    waktu_sekarang = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        # Pura-puranya pengunjung beneran yang lagi buka dashboard hacker Mas
        response = requests.get(TARGET_URL, headers=HEADERS, timeout=20)
        
        if response.status_code == 200:
            print(f"[{waktu_sekarang}] [SUCCESS] Tuyul tembus! HF mengira kita manusia. Status: 200")
        elif response.status_code == 429:
            print(f"[{waktu_sekarang}] [WARNING] HF mulai curiga (Too Many Requests). Kita rem dikit.")
        else:
            print(f"[{waktu_sekarang}] [INFO] HF merespon dengan status: {response.status_code}")
            
    except Exception as e:
        print(f"[{waktu_sekarang}] [ERROR] Aduh, tuyulnya kesandung: {str(e)}")

if __name__ == "__main__":
    print(f"--- ROBOT PENYAMAR CLAWCLOUD AKTIF ---")
    print(f"Targeting: {TARGET_URL}")
    print("---------------------------------------")
    
    while True:
        ketuk_pintu()
        
        # Jeda 5 menit (300 detik) biar sopan dan gak bikin HF Down lagi
        # 5 menit sekali udah cukup banget buat bikin Space tetep 'Running'
        time.sleep(300)
