from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.SecretSharing import Shamir
import binascii


def encrypt_AES_GCM(msg, secret_key):
    aes_cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, auth_tag = aes_cipher.encrypt_and_digest(msg)
    return (ciphertext, aes_cipher.nonce, auth_tag)


def decrypt_AES_GCM(encrypted_msg, secret_key):
    (ciphertext, nonce, auth_tag) = encrypted_msg
    aes_cipher = AES.new(secret_key, AES.MODE_GCM, nonce)
    plaintext = aes_cipher.decrypt_and_verify(ciphertext, auth_tag)
    return plaintext


message = b'a message to sign via AES-GCM'

secret_key = get_random_bytes(16)
print(f'Secret key:\n\t{binascii.hexlify(secret_key)}')

shares = Shamir.split(2, 5, secret_key)
print('Shared keys:')
for idx, share in shares:
    print(f'\t{binascii.hexlify(share)} ({idx})')

encrypted_msg = encrypt_AES_GCM(message, secret_key)
print('Encrypted message and parameters:')
print(f'\tAES with Galois/Counter Mode (GCM)')
print(f'\t{binascii.hexlify(encrypted_msg[0])} (ciphertext)')
print(f'\t{binascii.hexlify(encrypted_msg[1])} (nonce)')
print(f'\t{binascii.hexlify(encrypted_msg[2])} (auth_tag)')

combined_secret_key = Shamir.combine([shares[2], shares[4]])
decrypted_msg = decrypt_AES_GCM(encrypted_msg, combined_secret_key)
print('Decrypted message:')
print(f'\t{decrypted_msg}')