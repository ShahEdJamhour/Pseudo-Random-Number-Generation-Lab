from Cryptodome.Cipher import AES
from Cryptodome import Random

ciphertext = "d06bf9d0dab8e8ef880660d2af65aa82"
IV = "09080706050403020100A2B2C2D2E2F2".lower()
plaintext1 = "255044462d312e350a25d0d4c5d80a34"

with open('key_dict.txt') as f:
    keys = f.readlines()

for k in keys:
    key = (k[:-1]).decode("hex")
    cipher = AES.new(key, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(plaintext1)
    if ciphertext == encrypted.encode("hex")[0:32]:
        print("Match found")
        print("key: "+k[:-1])
        print("Ciphertext: " + ciphertext)
        print("Encrypted: " + encrypted.encode("hex"))