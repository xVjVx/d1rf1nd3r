import requests
import sys

if len(sys.argv) != 3:
    print("[!] Correct execution: python3 %s url wordlist"%(sys.argv[0]))
    sys.exit(0)

print(r"""
 _____  __ _____  ______ __ _   _ _____ ____  _____  
|  __ \/_ |  __ \|  ____/_ | \ | |  __ \___ \|  __ \ 
| |  | || | |__) | |__   | |  \| | |  | |__) | |__) |
| |  | || |  _  /|  __|  | | . ` | |  | |__ <|  _  / 
| |__| || | | \ \| |     | | |\  | |__| |__) | | \ \ 
|_____/ |_|_|  \_\_|     |_|_| \_|_____/____/|_|  \_\
""")


def dir_enum(url, wordlist):
    with open(wordlist, 'r') as file:
        words = file.read().splitlines()

    for word in words:
        subdir = url + "/" + word
        try:
            request = requests.get(subdir)
        except KeyboardInterrupt:
            print("[-] Session closed")
            sys.exit(0)

        if request.status_code == 200:
            print("/" + word + "  " + "[-] 200 Ok!")
        elif request.status_code == 301:
            print("/" + word + "  " + "[-] 301 Moved Permanently")
        elif request.status_code == 302:
            print("/" + word + "  " + "[-] 302 Found")
        elif request.status_code == 401:
            print("/" + word + "  " + "[-] 401 Unauthorized")
        elif request.status_code == 500:
            print("/" + word + "  " + "[-] 500 Internal Server Error")
        elif request.status_code == 502:
            print("/" + word + "  " + "[-] 502 Bad Gateway")


def main():

    url = sys.argv[1]
    wordlist = sys.argv[2]

    print("[-] Enumerating " + url + "...")
    dir_enum(url, wordlist)


if __name__ == '__main__':
    main()