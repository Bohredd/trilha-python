import hashlib

menu = int(input(
    """
    DIGITE O TIPO DE HASH!
    [1] MD5
    [2] SHA1
    [3] SHA256
    [4] SHA512
    """))

string = str(input("Digite a string para transformar em hash: "))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print(f'Sua hash é: {resultado.hexdigest()}')
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print(f'Sua hash é: {resultado.hexdigest()}')
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print(f'Sua hash é: {resultado.hexdigest()}')
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print(f'Sua hash é: {resultado.hexdigest()}')
else:
    print("Erro!")