import base64
from Crypto.Cipher import AES

payload = "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"
key = input('[默认"kPH+bIxk5D2deZiIxcaaaA="]请输入密钥：') or 'kPH+bIxk5D2deZiIxcaaaA=='
key = base64.b64decode(key)
if len(key)!=16:
    exit('密钥不足16位')

while True:
    payload = input('输入rememberMe：')
    decoded_data = base64.b64decode(payload)
    iv = decoded_data[:16]
    cipher_text = decoded_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    a = cipher.decrypt(cipher_text)
    if len(set(a[-a[-1]:])) != 1:
        print('填充位错误')
    decrypted_data = a[0:-a[-1]]
    print('\n'*10)
    print(decrypted_data)
    print('\n偏移：%s' % base64.b64encode(iv).decode())
    print('偏移HEX', end='：')
    for f1 in iv:
        print(str(hex(f1)[2:]), end=' ')
    print('\n')
    print('密钥：%s' % base64.b64encode(key).decode())
    print('密钥HEX', end='：')
    for f1 in key:
        print(str(hex(f1)[2:]), end=' ')
    print('\n')
    xk1=a[a.find(b'\t\xce')+2:a.find(b'pt\x00\x01apw\x01')]
    xk2=input(f'有一份{len(xk1)}字节的文件，输入导出文件名：') or False
    if xk2:
        open(xk2+'.class','wb').write(xk1)
    print('\n'*10)
