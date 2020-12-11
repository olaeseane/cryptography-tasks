from fastecdsa import keys, curve, ecdsa
from hashlib import sha256


def get_der_format(r, s):
    '''encode ECDSA signatures to Distinguished Encoding Rules (DER) format'''
    hr = hex(r)[2:]
    hs = hex(s)[2:]
    der_s = '02'+hex(len(hr))[2:]+hr + '02'+hex(len(hs))[2:]+hs
    return '30' + hex(len(der_s))[2:]+der_s


message = "a message to sign via ECDSA"

# generate a private key for curve P256
priv_key = keys.gen_private_key(curve.P256)
# get the public key corresponding to the private key we just generated
pub_key = keys.get_public_key(priv_key, curve.P256)
# standard signature, returns two integers
r, s = ecdsa.sign(message, priv_key, hashfunc=sha256)
# should return True as the signature we just generated is valid.
valid = ecdsa.verify((r, s), message, pub_key, hashfunc=sha256)

print(f'A message to sign = "{message}"')
print(f'Private key = {priv_key}')
print(f'Public key (X) = {pub_key.x}')
print(f'Public key (Y) = {pub_key.y}')
print(f'Signature (r) = {r}')
print(f'Signature (s) = {s}')
print(f'Signature (DER) = {get_der_format(r,s)}')
print(f'Is the signature valid? {valid}')
