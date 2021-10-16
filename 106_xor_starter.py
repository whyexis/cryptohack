#!/usr/bin/python3

string = "label"
key = 13
result = ''.join(chr(ord(c) ^ key) for c in string)

print("crypto{" + result + "}")
