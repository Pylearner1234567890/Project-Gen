import secrets
import binascii
import time
import subprocess

subprocess.run(['python', 'error check.py'])


# THIS IS A SCRIPT
def generate_iv() -> object:
    # Generate a random IV (16 bytes for AES)
    iv_bytes: bytes = secrets.token_bytes(16)
    iv_hex: str = binascii.hexlify(iv_bytes).decode("utf-8")
    return iv_hex


random_iv: object = generate_iv()
print('Random IV:', random_iv)
time.sleep(128)
print('EXIT PLS')
# 6A-61-79-20-62-65-61-6E this is nothing :>
