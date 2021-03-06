
import sys 
import requests

bck_extensions = [

".bak", ".backup", ".bac", ".zip", ".tar", ".jar", ".log", ".swp",
"~", ".old", ".~bk", ".orig", ".tmp", ".exe", ".0", ".1", ".2", ".3", 
".gz", ".bz2", ".7z", ".s7z", ".lz", ".z", ".lzma", ".lzo", ".apk",
".cab", ".rar", ".war",".ear", ".tar.gz", ".tgz", ".tar.z", ".tar.bz2",
".tbz2", ".tar.lzma", ".tlz", ".zipx", ".iso", ".src", ".dev", ".a", 
".a", ".ar",".cbz", ".cpio", ".shar", ".lbr", ".lbr", ".mar", ".f", 
".rz", ".sfark", ".xz", ".ace", ".afa", ".alz", ".arc", ".arj", ".ba",
".bh", ".cfs", ".cpt", ".dar", ".dd", ".dgc", ".dmg", ".gca", ".ha",
".hki", ".ice", ".inc", ".j", ".kgb", ".lhz", ".lha", ".lzk", ".pak",
".partimg.", ".paq6", ".paq7", ".paq8", ".pea", ".pim", ".pit", ".qda",
".rk", ".sda", ".sea", ".sen", ".sfx", ".sit", ".sitx", ".sqx", "s.xz", 
".tar.7z", ".tar.xz", ".uc", ".uc0", ".uc2", ".ucn", ".ur2", ".ue2",
".uca", ".uha", ".wim", ".xar", ".xp3", ".yz1", ".zoo", ".zpaq", ".z1z",
".include"

]

def findBackupFile(url):
    
    index = 0
    finded = False

    while index < len(bck_extensions) and not finded:
        bck_file = url + bck_extensions[index]
        print(bck_file)
        response = requests.get(bck_file).text
        if not "404 Not Found" in response:
            finded = True
        index += 1

    return finded

def main():

    URL_FILE = "http://challenge01.root-me.org/web-serveur/ch11/index.php"

    print("[*] Testing extensions...\n")
    
    if not findBackupFile(URL_FILE):
        print("\n[x] File not found")
        sys.exit(1)

    print("\n[+] File found")

if __name__ == "__main__":
    main()
