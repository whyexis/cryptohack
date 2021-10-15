#!/usr/bin/python3

import base64

# Hex string
s = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Decode hex into bytes
b = bytes.fromhex(s)

# Encode into base64
b64 = base64.b64encode(b)

# Print flag
print(str(b64, "utf-8"))
