import random
import time
f=open("log.txt",mode='a+')
person=['john',"jack","ali","sara","ziad"]
while True:
    r=random.choice(person)
    s=r+" : hi thats mee!\n"
    f.write(s)
    f.seek(0)
    print(f.read())
    time.sleep(2)
