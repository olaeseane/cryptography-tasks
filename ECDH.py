from tinyec.ec import SubGroup, Curve, Point
import secrets


def compress(pub_key):
    return hex(pub_key.x) + hex(pub_key.y % 2)[2:]


# named curve
name = 'secp256k1'
# modulus
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
# order; the count of all possible EC points
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
# the constant "a" in y^2 ≡ x^3 + a*x + b (mod p)
a = 0x0000000000000000000000000000000000000000000000000000000000000000
# the constant "b" in y^2 ≡ x^3 + a*x + b (mod p)
b = 0x0000000000000000000000000000000000000000000000000000000000000007
# the curve generator point G {x, y}
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
     0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
# cofactor
h = 1
# Alice_Pubkey:
x = 14910571678862872761868841217294607909892752044215461914879649677693867889072
y = 62514830396634191665984879881213930227864491048359651030093312396718750313589

# calculate my keys
curve = Curve(a, b, SubGroup(p, g, n, h), name)
my_priv_key = secrets.randbelow(curve.field.n)
my_pub_key = my_priv_key * curve.g
print(f'my private key: {my_priv_key}')
print(f'my public key: {(my_pub_key.x, my_pub_key.y)}')

# calculate shared secret = My_Privkey * Alice_Pubkey
shared_key = my_priv_key * Point(curve, x, y)
print(f'our shared key: {(shared_key.x, shared_key.y)}')

