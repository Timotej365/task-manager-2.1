import time
import requests
import sys

SERVER_URL = "https://task-manager-2-1.vercel.app/"

def cakat_na_server(timeout=60, interval=5):
    print(f"\n⏳ Prebieha prebudenie servera Render...")
    sys.stdout.flush()
    cas = 0
    while cas < timeout:
        try:
            odpoved = requests.get(SERVER_URL, timeout=5)
            if odpoved.status_code == 200:
                print("✅ Server je pripravený. Pokračujeme v testoch.")
                sys.stdout.flush()
                return
        except requests.exceptions.RequestException:
            pass
        print(f"🔁 Server zatiaľ neodpovedá. Čakám {interval} sekúnd...")
        sys.stdout.flush()
        time.sleep(interval)
        cas += interval
    raise Exception("❌ Server sa nezobudil včas.")
