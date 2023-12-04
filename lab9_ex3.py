import hmac
import hashlib
import base64

def string_to_bytearray(s):
    message_bytearray = bytearray();
    message_bytearray.extend(map(ord, s))
    return message_bytearray

key = "key"
message = "The quick brown fox jumps over the lazy dog"

print(F'HMAC_SHA256({key}, "{message}")')
h = hmac.new( string_to_bytearray(key), string_to_bytearray(message), hashlib.sha256)
print( h.hexdigest() )
first_digest = h.hexdigest()

print()
print(F'HMAC_SHA3_256({key}, "{message}")')
h = hmac.new( string_to_bytearray(key), string_to_bytearray(message), hashlib.sha3_256)
print( h.hexdigest() )

print()
print(F'HMAC_SHA512({key}, "{message}")')
h = hmac.new( string_to_bytearray(key), string_to_bytearray(message), hashlib.sha512)
print( h.hexdigest() )

print()
print(F'HMAC_SHA3_512({key}, "{message}")')
h = hmac.new( string_to_bytearray(key), string_to_bytearray(message), hashlib.sha3_512)
print( h.hexdigest() )

print("walidacja:")
print(F'HMAC_SHA256({key}, "{message}")')
h = hmac.new( string_to_bytearray(key), string_to_bytearray(message), hashlib.sha256)
if h.hexdigest() == first_digest:
    print(f'the message "{message}" is authentic')