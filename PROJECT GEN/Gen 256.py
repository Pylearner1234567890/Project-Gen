import secrets
import binascii
import time
import subprocess

subprocess.run(['python', 'error check.py'])


# THIS IS A SCRIPT!
def generate_aes_key() -> object:
    aes_key_bytes: bytes = secrets.token_bytes(32)
    aes_key_hex: str = binascii.hexlify(aes_key_bytes).decode('utf-8')
    return aes_key_hex


random_aes_key: object = generate_aes_key()
print('Random AES Key:', random_aes_key)
time.sleep(128)
# this is because when I ran this code it only pops up and then immediately closes
# 6A-61-79-20-62-65-61-6E this is nothing :>
