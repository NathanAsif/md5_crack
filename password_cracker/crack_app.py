import hashlib
from hmac import digest

flag = 0

pass_hash = input("Enter your md5 hash: ")

wordlist = input("Enter your wordlist: ")

try:
    passfile = open(wordlist, "r")
except:
    print("No wordlist found")
    quit()    

for word in passfile:
    wrd_enc = word.encode("utf-8")
    digest = hashlib.md5(wrd_enc.strip()).hexdigest()

    if digest == pass_hash:
        print("Password is found!")
        print("Password is: " + word)
        flag = 1
        break

if flag == 0:
    print("passphrase / password is not found")
    quit()