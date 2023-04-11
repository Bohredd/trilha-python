import hashlib # para Utilizar a bilbioteca de hashes

arquivo1 = open('a.txt', 'rb')
arquivo2 = open('b.txt', 'rb')

hash1 = hashlib.new('ripemd160') #ripemd160 é um algoritmo hash de 160 bits

hash1.update(arquivo1.read())

hash2 = hashlib.new('ripemd160')

hash2.update(arquivo2.read())

if hash1.digest() != hash2.digest(): #digest é o resumo do hash 
    print(f'O arquivo : {arquivo1} é diferente do arquivo: {arquivo2}')
else:
    print(f"O arquivo : {arquivo1} é igual ao arquivo: {arquivo2}")