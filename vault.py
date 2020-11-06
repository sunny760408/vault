# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import base64
import requests
import json

#轉base64
id = "A123456789".encode("UTF-8")
id_64 = base64.b64encode(id).decode("UTF-8")
print("原始字串:A123456789")
print("base64編碼:"+id_64)


data =  '{"plaintext": "'+id_64+'"}'
headers = {
    'X-Vault-Token': '123456wersdfcvb'
}

#送給Vault加密
response = requests.post('http://IP:8200/v1/shawn-transit/encrypt/id', headers=headers, data=data)
j = json.loads(response.text)
j_encrypt = j["data"]["ciphertext"]
print("Vault加密:"+j_encrypt)

#放到KV shawn-kv/shawn/id
kv = '{"data":{"id":"'+j_encrypt+'"}}'
kv_response = requests.post('http://IP:8200/v1/shawn-kv/data/shawn/id', headers=headers, data=kv)
print("放到KV:"+kv_response.text)

#取值
get_kv_response = requests.get('http://IP:8200/v1/shawn-kv/data/shawn/id', headers=headers)
j_get = json.loads(get_kv_response.text)
j_get_kv = j_get["data"]["data"]["id"]
print("取值:"+j_get_kv)
