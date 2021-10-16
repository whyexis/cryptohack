#!/usr/bin/python3

k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k1k2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flagk1k3k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

def xor(input1, input2):
    hex1 = bytes.fromhex(input1)
    hex2 = bytes.fromhex(input2)
    return bytes(a ^ b for a, b in zip(hex1, hex2)).hex()

k2 = xor(k1k2, k1)
k3 = xor(k2k3, k2)
flag = xor(xor(xor(flagk1k3k2, k2), k3), k1)

print(str(bytes.fromhex(flag), "utf-8"))
