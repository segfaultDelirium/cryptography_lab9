

# this can be installed by "pip install pycryptodome"
from Crypto.Hash import SHAKE128, SHAKE256

print("hello")

shake = SHAKE128.new()

message = ""
message_bytearray = bytearray();
message_bytearray.extend(map(ord, message))

# message2 = "The quick brown fox jumps over the lazy dof"
# message2_bytearray = bytearray();
# message2_bytearray.extend(map(ord, message2))

shake.update(message_bytearray)

print(f"SHAKE-128('{message}', 256)")
print(shake.read(256).hex())


shake = SHAKE128.new()
shake.update(message_bytearray)
print()
print(f"SHAKE-128('{message}', 512)")
print(shake.read(512).hex())
print()


shake = SHAKE256.new()

shake.update(message_bytearray)

print()
print(f"SHAKE-256('{message}', 512)")
print(shake.read(512).hex())


# print(shake.read(256).hex())