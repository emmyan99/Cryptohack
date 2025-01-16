import base64

hstr = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
b = bytes.fromhex(hstr)

key = base64.b64encode(b).decode('utf-8')

print(key)

