import os
import requests

GITHUB_RAW_URL = "https://raw.githubusercontent.com/omakhh/super-trader/main/super_trader.py"
LOCAL_FILENAME = "super_trader.py"

def download_update():
    print("🧠 Downloading latest version of Super Machine...")
    r = requests.get(GITHUB_RAW_URL)
    with open(LOCAL_FILENAME, 'wb') as f:
        f.write(r.content)
    print("🚀 Running local version of Super Machine...")
    os.system("python super_trader.py")

if __name__ == "__main__":
    download_update()